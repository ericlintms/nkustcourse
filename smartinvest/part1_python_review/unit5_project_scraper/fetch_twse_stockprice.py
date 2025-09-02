
# url: https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20250902&type=ALLBUT0999&response=json

import requests
import json
from datetime import datetime
import sqlite3
import re
from typing import List, Tuple, Any, Dict
from dataclasses import dataclass

def parse_change_html(html_str: str) -> Tuple[str, str]:
    """
    解析漲跌欄位的 HTML 標籤，提取顏色和符號

    Args:
        html_str (str): HTML 標籤字串

    Returns:
        tuple: (color, symbol) - 顏色和符號
    """
    if not html_str or html_str.strip() == '':
        return 'black', ' '

    # 使用正則表達式解析 HTML 標籤
    color_match = re.search(r"color:(\w+)", html_str)
    symbol_match = re.search(r">([+-]|\s)<", html_str)

    color = color_match.group(1) if color_match else 'black'
    symbol = symbol_match.group(1).strip() if symbol_match else ' '

    return color, symbol

@dataclass
class Stock:
    code: str
    name: str
    volume: str
    trades: str
    amount: str
    open_price: str
    high: str
    low: str
    close: str
    color: str
    symbol: str
    change_price: str
    bid_price: str
    bid_volume: str
    ask_price: str
    ask_volume: str
    pe_ratio: str

@dataclass
class MarketIndex:
    name: str
    close: str
    color: str
    symbol: str
    change_points: str
    change_percent: str
    note: str

def fetch_twse_data(date_str: str) -> Tuple[List[Stock], List[MarketIndex]]:
    """
    抓取台灣證券交易所特定日期的股市資料

    Args:
        date_str (str): 日期字串，格式為 YYYYMMDD，例如 '20250902'

    Returns:
        tuple: (stocks_list, indices_list) - 股票列表和指數列表
    """
    url = f"https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date={date_str}&type=ALLBUT0999&response=json"

    try:
        response: requests.Response = requests.get(url)
        response.raise_for_status()
        data: Dict[str, Any] = response.json()

        stocks: List[Stock] = []
        indices: List[MarketIndex] = []

        for table in data.get('tables', []):
            title = table.get('title', '')
            table_data = table.get('data', [])

            if '每日收盤行情' in title:
                # 解析股票資料
                for row in table_data:
                    if len(row) >= 16:
                        # 解析漲跌欄位的 HTML 標籤
                        color, symbol = parse_change_html(row[9])

                        stock = Stock(
                            code=row[0],
                            name=row[1],
                            volume=row[2].replace(',', ''),
                            trades=row[3].replace(',', ''),
                            amount=row[4].replace(',', ''),
                            open_price=row[5],
                            high=row[6],
                            low=row[7],
                            close=row[8],
                            color=color,
                            symbol=symbol,
                            change_price=row[10],
                            bid_price=row[11],
                            bid_volume=row[12].replace(',', ''),
                            ask_price=row[13],
                            ask_volume=row[14].replace(',', ''),
                            pe_ratio=row[15]
                        )
                        stocks.append(stock)

            elif '價格指數' in title:
                # 解析指數資料
                for row in table_data:
                    if len(row) >= 6:
                        # 解析漲跌欄位的 HTML 標籤
                        color, symbol = parse_change_html(row[2])

                        index = MarketIndex(
                            name=row[0],
                            close=row[1].replace(',', ''),
                            color=color,
                            symbol=symbol,
                            change_points=row[3].replace(',', ''),
                            change_percent=row[4],
                            note=row[5]
                        )
                        indices.append(index)

        return stocks, indices

    except requests.RequestException as e:
        print(f"網路請求錯誤: {e}")
        return [], []
    except json.JSONDecodeError as e:
        print(f"JSON 解析錯誤: {e}")
        return [], []

def save_to_database(stocks: List[Stock], indices: List[MarketIndex], db_path: str = 'twse_data.db') -> None:
    """
    將資料儲存到 SQLite 資料庫

    Args:
        stocks (list): Stock 物件列表
        indices (list): MarketIndex 物件列表
        db_path (str): 資料庫檔案路徑
    """
    conn: sqlite3.Connection = sqlite3.connect(db_path)
    cursor: sqlite3.Cursor = conn.cursor()

    # 建立股票資料表
    cursor.execute('DROP TABLE IF EXISTS stocks')
    cursor.execute('''
        CREATE TABLE stocks (
            code TEXT PRIMARY KEY,
            name TEXT,
            volume INTEGER,
            trades INTEGER,
            amount REAL,
            open_price REAL,
            high REAL,
            low REAL,
            close REAL,
            color TEXT,
            symbol TEXT,
            change_price REAL,
            bid_price REAL,
            bid_volume INTEGER,
            ask_price REAL,
            ask_volume INTEGER,
            pe_ratio REAL,
            date TEXT
        )
    ''')

    # 建立指數資料表
    cursor.execute('DROP TABLE IF EXISTS indices')
    cursor.execute('''
        CREATE TABLE indices (
            name TEXT PRIMARY KEY,
            close REAL,
            color TEXT,
            symbol TEXT,
            change_points REAL,
            change_percent REAL,
            note TEXT,
            date TEXT
        )
    ''')

    # 插入股票資料
    current_date: str = datetime.now().strftime('%Y-%m-%d')
    for stock in stocks:
        def safe_float(value: Any) -> float:
            try:
                return float(value) if value and value != '--' else 0.0
            except (ValueError, TypeError):
                return 0.0

        def safe_int(value: Any) -> int:
            try:
                return int(value) if value and value != '--' else 0
            except (ValueError, TypeError):
                return 0

        cursor.execute('''
            INSERT OR REPLACE INTO stocks
            (code, name, volume, trades, amount, open_price, high, low, close, color, symbol, change_price,
             bid_price, bid_volume, ask_price, ask_volume, pe_ratio, date)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            stock.code, stock.name, safe_int(stock.volume), safe_int(stock.trades), safe_float(stock.amount),
            safe_float(stock.open_price), safe_float(stock.high), safe_float(stock.low), safe_float(stock.close),
            stock.color, stock.symbol, safe_float(stock.change_price), safe_float(stock.bid_price), safe_int(stock.bid_volume),
            safe_float(stock.ask_price), safe_int(stock.ask_volume), safe_float(stock.pe_ratio), current_date
        ))

    # 插入指數資料
    for index in indices:
        cursor.execute('''
            INSERT OR REPLACE INTO indices
            (name, close, color, symbol, change_points, change_percent, note, date)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            index.name, safe_float(index.close), index.color, index.symbol, safe_float(index.change_points),
            safe_float(index.change_percent), index.note, current_date
        ))

    conn.commit()
    conn.close()
    print(f"資料已儲存到 {db_path}")

# 使用範例
if __name__ == "__main__":
    # 抓取指定日期的資料
    date: str = "20250902"
    stocks: List[Stock]
    indices: List[MarketIndex]
    stocks, indices = fetch_twse_data(date)

    print(f"抓取到 {len(stocks)} 支股票資料")
    print(f"抓取到 {len(indices)} 個指數資料")

    # 顯示前幾支股票
    for stock in stocks[:5]:
        print(stock)

    # 顯示前幾個指數
    for index in indices[:5]:
        print(index)

    # 儲存到資料庫
    save_to_database(stocks, indices)

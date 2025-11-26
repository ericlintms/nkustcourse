
# url: https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20250902&type=ALLBUT0999&response=json

import requests
import json
from datetime import datetime, timedelta
import sqlite3
import re
from typing import List, Tuple, Any, Dict
from dataclasses import dataclass

def parse_change_html(html_str: str) -> Tuple[str, str]:
    """
    解析漲跌欄位的 HTML 標籤，提取顏色和符號

    Args:
        html_str (str): HTML 標籤字串，例如 '<p style= color:green>-</p>'

    Returns:
        tuple: (color, symbol) - 顏色和符號
    """
    if not html_str or html_str.strip() == '':
        return 'black', ' '

    # 移除 HTML 標籤中的 Unicode 轉義序列 (如 \u002fp)
    html_str = html_str.replace('\\u002f', '/')
    
    # 使用正則表達式解析 HTML 標籤
    # 匹配 style= 後面的顏色（支持 color: 前有空格的情況）
    color_match = re.search(r"color\s*:\s*(\w+)", html_str)
    # 匹配 > 和 < 之間的符號
    symbol_match = re.search(r">([+-]|\s)<", html_str)

    color = color_match.group(1) if color_match else 'black'
    symbol = symbol_match.group(1) if symbol_match else ' '

    return color, symbol

@dataclass
class Stock:
    date: str
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
    date: str
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
                            date=date_str,
                            code=row[0],
                            name=row[1],
                            volume=row[2].replace(',', ''),
                            trades=row[3].replace(',', ''),
                            amount=row[4].replace(',', ''),
                            open_price=row[5].replace(',', ''),
                            high=row[6].replace(',', ''),
                            low=row[7].replace(',', ''),
                            close=row[8].replace(',', ''),
                            color=color,
                            symbol=symbol,
                            change_price=row[10],
                            bid_price=row[11].replace(',', ''),
                            bid_volume=row[12].replace(',', ''),
                            ask_price=row[13].replace(',', ''),
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
                            date=date_str,
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


def fetch_twse_data_range(start_date: str, end_date: str) -> Tuple[List[Stock], List[MarketIndex]]:
    """
    抓取台灣證券交易所指定日期範圍的股市資料

    Args:
        start_date (str): 開始日期字串，格式為 YYYYMMDD，例如 '20250901'
        end_date (str): 結束日期字串，格式為 YYYYMMDD，例如 '20250930'

    Returns:
        tuple: (stocks_list, indices_list) - 合併後的股票列表和指數列表
    """
    # 解析日期
    start_datetime = datetime.strptime(start_date, '%Y%m%d')
    end_datetime = datetime.strptime(end_date, '%Y%m%d')

    all_stocks: List[Stock] = []
    all_indices: List[MarketIndex] = []

    current_date = start_datetime

    while current_date <= end_datetime:
        # 只抓取交易日（週一到週五）
        if current_date.weekday() < 5:
            date_str = current_date.strftime('%Y%m%d')
            print(f"正在抓取 {date_str} 的資料...")

            stocks, indices = fetch_twse_data(date_str)

            if stocks:
                all_stocks.extend(stocks)
                print(f"  成功抓取 {len(stocks)} 支股票")

            if indices:
                all_indices.extend(indices)
                print(f"  成功抓取 {len(indices)} 個指數")
        else:
            date_str = current_date.strftime('%Y%m%d')
            print(f"跳過 {date_str} (非交易日)")

        current_date += timedelta(days=1)

    print(f"\n總計抓取 {len(all_stocks)} 筆股票資料和 {len(all_indices)} 筆指數資料")
    return all_stocks, all_indices

def save_to_database(stocks: List[Stock], indices: List[MarketIndex], db_path: str = 'twse_data.db') -> None:
    """
    將資料儲存到 SQLite 資料庫，以日期+股號/指數名稱作為 PRIMARY KEY，避免覆蓋舊資料

    Args:
        stocks (list): Stock 物件列表
        indices (list): MarketIndex 物件列表
        db_path (str): 資料庫檔案路徑
    """
    def safe_float(value: Any) -> float:
        """安全地將值轉換為浮點數"""
        try:
            if value is None or value == '' or value == '--':
                return 0.0
            return float(value)
        except (ValueError, TypeError):
            return 0.0

    def safe_int(value: Any) -> int:
        """安全地將值轉換為整數"""
        try:
            if value is None or value == '' or value == '--':
                return 0
            return int(float(value))  # 先轉成 float 再轉 int，以便處理小數情況
        except (ValueError, TypeError):
            return 0

    conn: sqlite3.Connection = sqlite3.connect(db_path)
    cursor: sqlite3.Cursor = conn.cursor()

    # 建立股票資料表（如果不存在）
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stocks (
            date TEXT NOT NULL,
            code TEXT NOT NULL,
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
            PRIMARY KEY (date, code)
        )
    ''')

    # 建立指數資料表（如果不存在）
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS indices (
            date TEXT NOT NULL,
            name TEXT NOT NULL,
            close REAL,
            color TEXT,
            symbol TEXT,
            change_points REAL,
            change_percent REAL,
            note TEXT,
            PRIMARY KEY (date, name)
        )
    ''')

    # 插入股票資料
    for stock in stocks:
        cursor.execute('''
            INSERT OR REPLACE INTO stocks
            (date, code, name, volume, trades, amount, open_price, high, low, close, color, symbol, change_price,
             bid_price, bid_volume, ask_price, ask_volume, pe_ratio)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            stock.date, stock.code, stock.name, safe_int(stock.volume), safe_int(stock.trades), safe_float(stock.amount),
            safe_float(stock.open_price), safe_float(stock.high), safe_float(stock.low), safe_float(stock.close),
            stock.color, stock.symbol, safe_float(stock.change_price), safe_float(stock.bid_price), safe_int(stock.bid_volume),
            safe_float(stock.ask_price), safe_int(stock.ask_volume), safe_float(stock.pe_ratio)
        ))

    # 插入指數資料
    for index in indices:
        cursor.execute('''
            INSERT OR REPLACE INTO indices
            (date, name, close, color, symbol, change_points, change_percent, note)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            index.date, index.name, safe_float(index.close), index.color, index.symbol, safe_float(index.change_points),
            safe_float(index.change_percent), index.note
        ))

    conn.commit()
    conn.close()
    print(f"資料已儲存到 {db_path}")

def example_fetch_single_date(date: str) -> None:
    """
    示範1: 抓取單一日期的股市資料並儲存

    Args:
        date (str): 日期字串，格式為 YYYYMMDD
    """
    print("="*50)
    print("示範1: 抓取單一日期的資料")
    print("="*50)
    
    stocks, indices = fetch_twse_data(date)

    print(f"\n抓取到 {len(stocks)} 支股票資料")
    print(f"抓取到 {len(indices)} 個指數資料")

    # 顯示前幾支股票
    print("\n前 3 支股票:")
    for stock in stocks[:3]:
        print(f"  {stock.code} {stock.name}: 收盤 {stock.close} ({stock.symbol}{stock.change_price})")

    # 顯示前幾個指數
    print("\n前 3 個指數:")
    for index in indices[:3]:
        print(f"  {index.name}: 收盤 {index.close} ({index.symbol}{index.change_points})")

    # 儲存單日資料到資料庫
    save_to_database(stocks, indices)

def example_fetch_date_range(start_date: str, end_date: str) -> None:
    """
    示範2: 抓取日期範圍的股市資料並逐日儲存

    Args:
        start_date (str): 開始日期字串，格式為 YYYYMMDD
        end_date (str): 結束日期字串，格式為 YYYYMMDD
    """
    print("\n" + "="*50)
    print("示範2: 抓取日期範圍的資料")
    print("="*50)

    # 解析日期
    start_datetime = datetime.strptime(start_date, '%Y%m%d')
    end_datetime = datetime.strptime(end_date, '%Y%m%d')

    current_date = start_datetime

    while current_date <= end_datetime:
        # 只抓取交易日（週一到週五）
        if current_date.weekday() < 5:
            date_str = current_date.strftime('%Y%m%d')
            print(f"正在抓取 {date_str} 的資料...")

            stocks, indices = fetch_twse_data(date_str)

            if stocks:
                print(f"  成功抓取 {len(stocks)} 支股票")

            if indices:
                print(f"  成功抓取 {len(indices)} 個指數")

            # 立即將該日資料寫入資料庫
            if stocks or indices:
                save_to_database(stocks, indices)
        else:
            date_str = current_date.strftime('%Y%m%d')
            print(f"跳過 {date_str} (非交易日)")

        current_date += timedelta(days=1)


# 使用範例
if __name__ == "__main__":
    # 示範1: 抓取單一日期
    # example_fetch_single_date("20251028")

    # 示範2: 抓取日期範圍
    example_fetch_date_range("20250901", "20251112")



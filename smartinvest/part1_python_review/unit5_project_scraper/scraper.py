# 專案: 股市資訊爬蟲進階

import requests
from bs4 import BeautifulSoup
import csv

class StockScraper:
    def __init__(self, stock_id):
        self.stock_id = stock_id
        self.url = f"https://finance.yahoo.com/quote/{stock_id}"

    def _send_request(self):
        try:
            # 加入 headers 模擬瀏覽器行為
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
            response = requests.get(self.url, headers=headers)
            # 如果請求不成功 (e.g., 404 Not Found), 引發 HTTPError
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"抓取 {self.url} 時發生錯誤: {e}")
            return None

    def parse_price(self, response):
        if response is None:
            return None
        
        try:
            soup = BeautifulSoup(response.text, 'html.parser')
            # 這裡的 selector 需要根據實際網頁結構調整
            # 注意: Yahoo Finance 的網頁結構經常變動，這個 selector 可能會失效
            price_selector = 'Fw(b) Fz(36px) Mb(-4px) D(ib)'
            price_element = soup.find('fin-streamer', {'class': price_selector})
            
            if price_element:
                return price_element.text
            else:
                print("找不到價格元素，可能是網頁結構已變更")
                return None
        except Exception as e:
            print(f"解析價格時發生錯誤: {e}")
            return None

    def get_current_price(self):
        """主流程: 發送請求並解析價格"""
        print(f"正在抓取 {self.stock_id} 的股價...")
        response = self._send_request()
        price = self.parse_price(response)
        return price

    def save_to_csv(self, data):
        file_path = f'{self.stock_id}_data.csv'
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['StockID', 'Price'])
            writer.writerow(data)
        print(f"資料已儲存至 {file_path}")


if __name__ == '__main__':
    # 以蘋果公司 (AAPL) 為例
    scraper = StockScraper('AAPL')
    price = scraper.get_current_price()

    if price:
        print(f"取得 {scraper.stock_id} 的目前價格為: {price}")
        scraper.save_to_csv([scraper.stock_id, price])
    else:
        print(f"無法取得 {scraper.stock_id} 的價格")

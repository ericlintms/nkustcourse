# 投影片 3/4: 專案藍圖 - `StockScraper` Class 設計

我們要設計一個 `StockScraper` Class，它應該包含...

## 屬性 (Attributes)

* `stock_id`: 要抓取的股票代號 (e.g., "AAPL")
* `url`: 根據股票代號組合出來的目標網址

---

## 方法 (Methods)

* `__init__(self, stock_id)`: 建構函式，初始化股票代號和 URL。

* `_send_request(self)`:
  * **私有方法** (用底線 `_` 開頭是一種慣例)。
  * 負責發送網路請求，並處理網路相關的例外 (`requests.exceptions.RequestException`)。

* `parse_price(self, response)`:
  * 負責解析 HTML 回應，從中找到價格。
  * 使用 `BeautifulSoup` 來定位元素。
  * 處理解析時可能發生的錯誤。

* `get_current_price(self)`:
  * **公開的主要方法**。
  * 負責協調 `_send_request` 和 `parse_price` 來完成整個抓取流程。

* `save_to_csv(self, data)`:
  * 將傳入的資料寫入 CSV 檔案。
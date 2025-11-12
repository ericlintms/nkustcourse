# 單元 5: API 伺服器 - FastAPI

回測是在歷史資料上進行的。如果我們想讓策略「活」起來，接收即時請求或觸發交易，就需要一個 API 伺服器。

## 學習目標

- 了解什麼是 API
- 學會使用 FastAPI 建立一個簡單的 Web API
- 了解如何定義路徑與處理請求

### 內容

1. **什麼是 API (Application Programming Interface)？**
    - 應用程式之間的溝通橋樑。
    - Web API: 透過 HTTP 協定溝通。
2. **FastAPI 介紹**
    - 一個現代、高效能的 Python Web 框架。
    - 優點：速度快、自動生成互動式 API 文件 (Swagger UI)、語法簡潔。
    - 安裝: `pip install fastapi "uvicorn[standard]"`
3. **建立你的第一個 API**
    - `main.py` 的基本結構。
    - 使用 `uvicorn` 啟動伺服器。
    - 路徑操作 (Path Operation) 與裝飾器 (`@app.get`)。
4. **路徑參數與查詢參數**
    - 路徑參數：`/stocks/{stock_id}`
    - 查詢參數：`/search?q=keyword`

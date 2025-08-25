# 範例 2: 路徑參數與查詢參數

# 檔名: main.py (可以接續在範例1後面)

from fastapi import FastAPI
from typing import Union

app = FastAPI()

# --- 模擬一個股票資料庫 ---
db = {
    "2330": {"name": "TSMC", "price": 600},
    "2454": {"name": "MediaTek", "price": 900}
}

# --- 1. 路徑參數 (Path Parameters) ---
# 用大括號 {} 來定義路徑中的變數
# 參數會直接傳入函式中
@app.get("/stocks/{stock_id}")
def get_stock_info(stock_id: str):
    if stock_id in db:
        return db[stock_id]
    return {"error": "Stock not found"}

# --- 2. 查詢參數 (Query Parameters) ---
# 不在路徑中的函式參數，會被自動視為查詢參數
# 格式: /path?key1=value1&key2=value2
@app.get("/search")
def search_stocks(q: Union[str, None] = None, limit: int = 10):
    # q: 搜尋關鍵字，可以是字串，也可以是 None (如果使用者沒提供)
    # limit: 回傳筆數上限，預設值為 10
    
    results = []
    if q:
        for stock_id, info in db.items():
            if q.lower() in info['name'].lower():
                results.append({stock_id: info})
    else:
        results = [db]

    return {"query": q, "limit": limit, "results": results[:limit]}

# --- 如何測試 ---
# 1. 執行 uvicorn main:app --reload
# 2. 路徑參數:
#    - http://127.0.0.1:8000/stocks/2330
#    - http://127.0.0.1:8000/stocks/9999
# 3. 查詢參數:
#    - http://127.0.0.1:8000/search?q=tsmc
#    - http://127.0.0.1:8000/search?q=tek&limit=1
#    - http://127.0.0.1:8000/search (不給 q)

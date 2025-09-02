# 這個練習需要一個 Python 腳本和一個 HTML 範本檔案。
# 這個 .py 檔案會自動建立所需的 `templates` 資料夾和 HTML 檔案。

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os

# --- 檔案與資料夾設定 ---
TEMPLATE_DIR = "templates"
TEMPLATE_NAME = "stock_list.html"

# 如果 templates 資料夾不存在，就建立它
if not os.path.exists(TEMPLATE_DIR):
    os.makedirs(TEMPLATE_DIR)

# 定義 HTML 範本的內容
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Stock Tickers</title>
</head>
<body>
    <h1>Available Stock Tickers</h1>
    <ul>
        {# 這是一個 Jinja2 的 for 迴圈 #}
        {% for ticker in tickers %}
            <li>{{ ticker }}</li>
        {% endfor %}
    </ul>
</body>
</html>
"""

# 將 HTML 內容寫入範本檔案
with open(os.path.join(TEMPLATE_DIR, TEMPLATE_NAME), "w", encoding="utf-8") as f:
    f.write(html_content)

# --- FastAPI 應用程式設定 ---
app = FastAPI()
templates = Jinja2Templates(directory=TEMPLATE_DIR)

@app.get("/stocks", response_class=HTMLResponse)
async def read_stocks(request: Request):
    # 這是要傳遞到範本的數據
    stock_tickers = ["AAPL", "GOOG", "MSFT", "TSLA", "NVDA"]
    
    # 渲染範本，並傳入 request 和數據
    return templates.TemplateResponse(TEMPLATE_NAME, {
        "request": request, 
        "tickers": stock_tickers
    })

print("範本檔案建立完成。")
print("請在終端機執行: uvicorn part3_unit6_sp_answer:app --reload")
print("然後在瀏覽器打開: http://127.0.0.1:8000/stocks")

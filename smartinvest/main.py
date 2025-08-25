# 範例 1: 在 FastAPI 中使用 Jinja2

# --- 專案結構 ---
# /your_project
#  |-- main.py
#  |-- /templates
#      |-- index.html

# --- 1. 安裝 Jinja2 ---
# pip install jinja2

# --- 2. 建立 FastAPI 主程式 (main.py) ---
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# 告訴 FastAPI 模板檔案放在 "templates" 這個目錄下
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # 準備要傳遞到模板中的資料
    data = {
        "page_title": "我的第一個模板網頁",
        "user_name": "SmartInvest"
    }
    
    # request: 必須傳入的請求物件
    # "index.html": 模板檔案的名稱
    # {"request": request, **data}: 傳遞給模板的內容
    #    - context 字典中必須包含 "request": request
    return templates.TemplateResponse("index.html", {"request": request, **data})


# --- 3. 建立模板檔案 (templates/index.html) ---
"""
<!DOCTYPE html>
<html>
<head>
    <title>{{ page_title }}</title>
</head>
<body>
    <h1>你好, {{ user_name }}!</h1>
    <p>歡迎來到 FastAPI 與 Jinja2 的世界。</p>
</body>
</html>
"""

# --- 4. 執行 ---
# uvicorn main:app --reload
# 打開瀏覽器 http://127.0.0.1:8000/

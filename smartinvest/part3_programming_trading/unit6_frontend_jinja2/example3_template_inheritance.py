# 範例 3: 模板繼承 (Template Inheritance)

# 當網站有多個頁面時，它們通常有共同的版型 (e.g., 頁首、頁尾、導覽列)。
# 模板繼承可以讓我們建立一個基礎版型，其他頁面再繼承它並填上自己的內容。

# --- 專案結構 ---
# /your_project
#  |-- main.py
#  |-- /templates
#      |-- base.html       (基礎版型)
#      |-- home.html       (首頁)
#      |-- about.html      (關於我們頁面)

# --- 1. FastAPI 主程式 (main.py) ---
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "page_name": "首頁"})

@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request, "company_name": "智慧投資公司"})


# --- 2. 建立基礎模板 (templates/base.html) ---
# 這個檔案定義了所有頁面的共同結構
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <title>{% block title %}預設標題{% endblock %}</title>
    <style> .header, .footer { background-color: #f2f2f2; padding: 10px; text-align: center; } </style>
</head>
<body>
    <div class="header">
        <h1>我的網站</h1>
        <nav><a href="/home">首頁</a> | <a href="/about">關於我們</a></nav>
    </div>

    <div class="content" style="padding: 20px;">
        {# --- 重點：定義一個可以被子模板覆寫的區塊 --- #}
        {% block content %}
        <p>這裡是預設的內容。</p>
        {% endblock %}
    </div>

    <div class="footer">
        <p>&copy; 2024 智慧投資公司</p>
    </div>
</body>
</html>
"""

# --- 3. 建立子模板 (templates/home.html) ---
"""
{# --- 重點 1：繼承 base.html --- #}
{% extends "base.html" %}

{# --- 重點 2：覆寫 base.html 中定義的 block --- #}
{% block title %}{{ page_name }} - 我的網站{% endblock %}

{% block content %}
    <h2>歡迎來到{{ page_name }}！</h2>
    <p>這是我們網站的主要內容。</p>
{% endblock %}
"""

# --- 4. 建立另一個子模板 (templates/about.html) ---
"""
{% extends "base.html" %}

{% block title %}關於我們{% endblock %}

{% block content %}
    <h2>關於 {{ company_name }}</h2>
    <p>我們致力於提供最棒的程式交易課程。</p>
{% endblock %}
"""

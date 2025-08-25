# 範例 2: 在模板中使用迴圈和條件判斷

# --- 專案結構 ---
# /your_project
#  |-- main.py
#  |-- /templates
#      |-- stocks.html

# --- 1. FastAPI 主程式 (main.py) ---
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/stocks", response_class=HTMLResponse)
async def list_stocks(request: Request):
    # 模擬從資料庫或回測結果中取得的資料
    stock_data = [
        {"id": "2330", "name": "台積電", "price": 600, "change": 5},
        {"id": "2454", "name": "聯發科", "price": 900, "change": -10},
        {"id": "2317", "name": "鴻海", "price": 100, "change": 0},
        {"id": "0050", "name": "元大台灣50", "price": 130, "change": 1.5}
    ]
    
    context = {
        "request": request,
        "stocks": stock_data
    }
    return templates.TemplateResponse("stocks.html", context)


# --- 2. 建立模板檔案 (templates/stocks.html) ---
"""
<!DOCTYPE html>
<html>
<head>
    <title>股票清單</title>
    <style>
        table { width: 100%; border-collapse: collapse; }
        th, td { border: 1px solid #dddddd; text-align: left; padding: 8px; }
        tr:nth-child(even) { background-color: #f2f2f2; }
        .positive { color: red; }
        .negative { color: green; }
    </style>
</head>
<body>
    <h1>今日股價</h1>
    <table>
        <thead>
            <tr>
                <th>代號</th>
                <th>名稱</th>
                <th>價格</th>
                <th>漲跌</th>
            </tr>
        </thead>
        <tbody>
            {% for stock in stocks %}
            <tr>
                <td>{{ stock.id }}</td>
                <td>{{ stock.name }}</td>
                <td>{{ stock.price }}</td>
                {# --- 條件判斷 --- #}
                {% if stock.change > 0 %}
                    <td class="positive">+{{ stock.change }}</td>
                {% elif stock.change < 0 %}
                    <td class="negative">{{ stock.change }}</td>
                {% else %}
                    <td>{{ stock.change }}</td>
                {% endif %}
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
"""

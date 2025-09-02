# 這個練習會自動建立所需的 `templates` 資料夾和 `dashboard.html` 檔案。

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os
import json

# --- 檔案與資料夾設定 ---
TEMPLATE_DIR = "templates"
TEMPLATE_NAME = "dashboard.html"

if not os.path.exists(TEMPLATE_DIR):
    os.makedirs(TEMPLATE_DIR)

# HTML 範本內容，內含 Chart.js 的 CDN 和渲染腳本
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Mini Dashboard</title>
    <!-- 從 CDN 引入 Chart.js -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <h1>Simple Stock Price Dashboard</h1>
    <div style="width: 75%; margin: auto;">
        <canvas id="myChart"></canvas>
    </div>

    <script>
        // 透過 Jinja2 的 tojson filter 將後端傳來的 Python dict 轉換為安全的 JSON 物件
        const chartData = {{ chart_data|tojson }};

        const ctx = document.getElementById('myChart').getContext('2d');
        
        new Chart(ctx, {
            type: 'bar', // 圖表類型為長條圖
            data: {
                labels: chartData.labels, // X軸標籤
                datasets: [{
                    label: 'Stock Price (USD)', // 數據集的標籤
                    data: chartData.data,       // Y軸數據
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true // Y軸從 0 開始
                    }
                }
            }
        });
    </script>
</body>
</html>
"""

with open(os.path.join(TEMPLATE_DIR, TEMPLATE_NAME), "w", encoding="utf-8") as f:
    f.write(html_template)

# --- FastAPI 應用程式 ---
app = FastAPI()
templates = Jinja2Templates(directory=TEMPLATE_DIR)

@app.get("/dashboard", response_class=HTMLResponse)
async def get_dashboard(request: Request):
    # 要在圖表中顯示的範例數據
    data_for_chart = {
        "labels": ["AAPL", "GOOG", "MSFT", "TSLA"],
        "data": [175.5, 138.2, 310.0, 255.8]
    }
    
    return templates.TemplateResponse(TEMPLATE_NAME, {
        "request": request,
        "chart_data": data_for_chart
    })

print("儀表板範本檔案建立完成。")
print("請在終端機執行: uvicorn part3_unit7_sp_answer:app --reload")
print("然後在瀏覽器打開: http://127.0.0.1:8000/dashboard")

# 專案範例: 交易儀表板 (簡化版)

# --- 專案結構 ---
# /dashboard_project
#  |-- main.py
#  |-- /templates
#      |-- dashboard.html

# --- 1. 安裝所需套件 ---
# pip install fastapi "uvicorn[standard]" jinja2 backtesting

# --- 2. 後端主程式 (main.py) ---
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from backtesting import Backtest, Strategy
from backtesting.test import SMA, GOOG
from backtesting.lib import crossover

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# --- 策略定義 (與之前相同) ---
class SmaCross(Strategy):
    n1 = 10
    n2 = 20
    def init(self):
        self.sma1 = self.I(SMA, self.data.Close, self.n1)
        self.sma2 = self.I(SMA, self.data.Close, self.n2)
    def next(self):
        if crossover(self.sma1, self.sma2):
            self.buy()
        elif crossover(self.sma2, self.sma1):
            self.sell()

# --- API 端點 ---
@app.get("/", response_class=HTMLResponse)
async def get_dashboard(request: Request):
    # 初始頁面，不帶任何結果
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.post("/run_backtest", response_class=HTMLResponse)
async def run_backtest(request: Request, fast_ma: int = Form(...), slow_ma: int = Form(...)):
    # 接收來自表單的參數
    class DynamicSmaCross(SmaCross):
        n1 = fast_ma
        n2 = slow_ma

    bt = Backtest(GOOG, DynamicSmaCross, cash=10000, commission=.002)
    stats = bt.run()

    # 準備要傳給前端的資料
    context = {
        "request": request,
        "stats": stats.to_dict(), # 將績效 Series 轉為字典
        "equity_curve": stats['_equity_curve']['Equity'].to_json() # 傳遞資金曲線數據
    }
    return templates.TemplateResponse("dashboard.html.j2", context)


# --- 3. 前端模板 (templates/dashboard.html) ---
# (請見下一個檔案)

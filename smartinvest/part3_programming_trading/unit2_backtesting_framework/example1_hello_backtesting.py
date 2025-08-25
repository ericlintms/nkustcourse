# 範例 1: backtesting.py Hello World

# 需要先安裝: pip install backtesting
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA, GOOG

# 1. 定義你的交易策略
# 策略必須繼承 Strategy
class SmaCross(Strategy):
    # n1 和 n2 是可以最佳化的策略參數
    n1 = 10
    n2 = 20

    def init(self):
        # 在策略初始化時，計算你需要的指標
        # self.I() 是一個方便的函式，可以將任何函式轉換為 backtesting.py 的指標
        self.sma1 = self.I(SMA, self.data.Close, self.n1)
        self.sma2 = self.I(SMA, self.data.Close, self.n2)

    def next(self):
        # 在每一根 K 棒都會被呼叫
        # crossover(series1, series2) 是一個內建函式，
        # 當 series1 由下往上穿越 series2 時會回傳 True
        if crossover(self.sma1, self.sma2):
            self.buy() # 黃金交叉，買入
        elif crossover(self.sma2, self.sma1):
            self.sell() # 死亡交叉，賣出


# --- 執行回測 ---

# 2. 準備資料 (backtesting.py 內建了 Google 的股價資料做為範例)
# 資料必須是 Pandas DataFrame，且欄位名稱為 Open, High, Low, Close (首字大寫)
print("--- 範例資料 (GOOG) ---")
print(GOOG.tail())

# 3. 建立 Backtest 物件
# cash: 初始資金
# commission: 手續費率 (0.002 = 0.2%)
bt = Backtest(GOOG, SmaCross, cash=10000, commission=.002)

# 4. 執行回測
stats = bt.run()

# 5. 印出績效報告
print("\n--- 回測結果 ---")
print(stats)

# 6. 繪製績效圖表 (會自動開啟瀏覽器)
bt.plot()

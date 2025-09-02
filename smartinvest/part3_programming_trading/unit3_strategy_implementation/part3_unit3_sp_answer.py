from backtesting import Strategy, Backtest
from backtesting.lib import crossover
from backtesting.test import SMA, GOOG

class SmaCrossStrategy(Strategy):
    # 定義策略參數，方便之後進行優化
    fast_sma_period = 10
    slow_sma_period = 20

    def init(self):
        # 取得收盤價數據
        close_price = self.data.Close
        # 使用 self.I 方法計算指標，這樣函式庫才能追蹤它們
        self.fast_sma = self.I(SMA, close_price, self.fast_sma_period)
        self.slow_sma = self.I(SMA, close_price, self.slow_sma_period)

    def next(self):
        # 檢查快線是否向上穿越慢線
        if crossover(self.fast_sma, self.slow_sma):
            self.buy()  # 執行買入
        
        # 檢查快線是否向下穿越慢線
        elif crossover(self.slow_sma, self.fast_sma):
            self.sell() # 執行賣出 (或平倉)

# --- 執行回測 ---
# 使用函式庫內建的 Google 股票數據進行測試
bt = Backtest(GOOG, SmaCrossStrategy, 
              cash=10000, commission=.002)

# 執行並取得結果
stats = bt.run()

print("--- SMA 均線交叉策略回測結果 ---")
print(stats)

# 你也可以取消註解以下這行來繪製結果圖表
# bt.plot()

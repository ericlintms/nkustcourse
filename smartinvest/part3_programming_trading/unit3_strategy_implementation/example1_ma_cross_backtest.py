# 範例 1: 回測移動平均線交叉策略

from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA, GOOG

class MovingAverageCross(Strategy):
    # 策略參數
    fast_ma_period = 10
    slow_ma_period = 30

    def init(self):
        # 計算快、慢兩條移動平均線
        self.fast_ma = self.I(SMA, self.data.Close, self.fast_ma_period)
        self.slow_ma = self.I(SMA, self.data.Close, self.slow_ma_period)

    def next(self):
        # 如果手上沒有部位，且發生黃金交叉，就買入
        if not self.position and crossover(self.fast_ma, self.slow_ma):
            self.buy()
        
        # 如果手上有部位，且發生死亡交叉，就賣出
        elif self.position and crossover(self.slow_ma, self.fast_ma):
            self.sell()

# --- 執行回測 ---
bt = Backtest(GOOG, MovingAverageCross, cash=10000, commission=.002)
stats = bt.run()

print("--- 移動平均線交叉策略回測結果 ---")
print(stats)
bt.plot()

# 範例 3: 加上停損停利

from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA, GOOG

class SmaCrossWithSlTp(Strategy):
    fast_ma_period = 10
    slow_ma_period = 30

    def init(self):
        self.fast_ma = self.I(SMA, self.data.Close, self.fast_ma_period)
        self.slow_ma = self.I(SMA, self.data.Close, self.slow_ma_period)

    def next(self):
        # 如果發生黃金交叉，就買入
        # 這次我們不檢查手上是否有部位，讓它可以加碼
        if crossover(self.fast_ma, self.slow_ma):
            # sl: 停損點 (stop-loss), 設定為當前價格的 95%
            # tp: 停利點 (take-profit), 設定為當前價格的 110%
            self.buy(sl=self.data.Close[-1] * 0.95, 
                     tp=self.data.Close[-1] * 1.10)
        
        # 死亡交叉時，關閉所有現有多頭部位
        # (不停損停利，直接平倉)
        elif crossover(self.slow_ma, self.fast_ma):
            self.position.close()

# --- 執行回測 ---
bt = Backtest(GOOG, SmaCrossWithSlTp, cash=10000, commission=.002)
stats = bt.run()

print("--- MA 交叉 + 停損停利策略回測結果 ---")
print(stats)
bt.plot()

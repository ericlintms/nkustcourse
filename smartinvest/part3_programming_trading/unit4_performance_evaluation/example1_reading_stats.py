# 範例 1: 解讀回測報告

from backtesting import Backtest, Strategy
from backtesting.test import SMA, GOOG

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

bt = Backtest(GOOG, SmaCross, cash=10000, commission=.002)
stats = bt.run()

# stats 是一個 Pandas Series，包含了所有的績效指標
print("--- 回測報告 (Pandas Series) ---")
print(stats)

# --- 手動存取特定指標 ---
print("\n--- 重點指標解析 ---")

# 總報酬率 (Return [%])
# 整個回測期間，你的資金成長了多少個百分比
print(f"總報酬率: {stats['Return [%]']:.2f}%")

# 年化報酬率 (Return (Ann.) [%])
# 將總報酬率轉換為年平均報酬率，更具可比性
print(f"年化報酬率: {stats['Return (Ann.) [%]']:.2f}%")

# 最大回撤 (Max. Drawdown [%])
# 策略從資金高點回落到低點的最大幅度，衡量策略可能面臨的最壞情況
# 這個值越低越好
print(f"最大回撤: {stats['Max. Drawdown [%]']:.2f}%")

# 夏普比率 (Sharpe Ratio)
# 衡量「風險調整後報酬」，數值越高代表策略越有效率 (CP值越高)
# 一般來說 > 1 算不錯，> 2 算很好
print(f"夏普比率: {stats['Sharpe Ratio']:.2f}")

# 勝率 (Win Rate [%])
# 獲利的交易次數 / 總交易次數
print(f"勝率: {stats['Win Rate [%]']:.2f}%")

# 總交易次數 (# Trades)
print(f"總交易次數: {stats['# Trades']}")

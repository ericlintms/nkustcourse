# 範例 2: 準備自己的資料

import pandas as pd
from backtesting import Backtest, Strategy

# --- 準備符合格式的資料 --- #
# 欄位名稱必須是 Open, High, Low, Close (大小寫敏感)
# 索引必須是時間格式
data = {
    'Open': [100, 102, 101, 105, 107, 106, 108, 110, 112, 109, 107, 105, 103, 106, 108],
    'High': [103, 104, 103, 106, 108, 107, 109, 111, 113, 110, 108, 106, 105, 107, 109],
    'Low': [99, 101, 100, 104, 106, 105, 107, 109, 110, 108, 106, 104, 102, 105, 107],
    'Close': [102, 101, 105, 107, 106, 108, 110, 112, 109, 107, 105, 103, 106, 108, 105]
}
index = pd.to_datetime(pd.date_range(start='2023-01-01', periods=15))
my_data = pd.DataFrame(data, index=index)

# --- 定義一個簡單的「今天漲就買，今天跌就賣」策略 (僅為示範) ---
class SimpleStrategy(Strategy):
    def init(self):
        pass

    def next(self):
        # 如果今天的收盤價 > 開盤價
        if self.data.Close[-1] > self.data.Open[-1]:
            # 如果手上沒有部位，就買入
            if not self.position:
                self.buy()
        # 如果今天的收盤價 < 開盤價
        elif self.data.Close[-1] < self.data.Open[-1]:
            # 如果手上有部位，就賣出
            if self.position:
                self.sell()


# --- 使用我們自己的資料進行回測 ---
bt = Backtest(my_data, SimpleStrategy, cash=10000, commission=0.001)
stats = bt.run()

print(stats)
bt.plot()

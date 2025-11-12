# 投影片 3/4: `Strategy` 類別詳解

## 所有交易邏輯的核心

你需要建立一個自己的 Class，並繼承 `backtesting.Strategy`。

```python
from backtesting import Strategy

class MyStrategy(Strategy):
    # --- 1. (可選) 定義策略參數 ---
    # 這些參數可以在執行回測時傳入，或在最佳化時使用
    ma_period = 20

    # --- 2. 實作 init() 方法 ---
    # 這個方法在回測開始時只會被執行一次
    def init(self):
        # 通常用來初始化你的指標
        self.ma = self.I(SMA, self.data.Close, self.ma_period)

    # --- 3. 實作 next() 方法 ---
    # 這個方法會在每一根 K 棒 (每一個時間點) 被呼叫一次
    # 這是你定義買賣邏輯的地方
    def next(self):
        if self.data.Close[-1] > self.ma[-1]:
            self.buy()
        else:
            self.sell()
```

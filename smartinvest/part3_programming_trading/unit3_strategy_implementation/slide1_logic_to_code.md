# 投影片 1/4: 將策略邏輯轉為程式碼

## 策略: 移動平均線黃金交叉買入，死亡交叉賣出

**人類語言的邏輯:**

1. 計算 10 日移動平均線 (快線) 和 30 日移動平均線 (慢線)。
2. 每天檢查：
    * 如果「快線」從下方穿越「慢線」(黃金交叉)，並且我手上沒有股票，就「買入」。
    * 如果「快線」從上方跌破「慢線」(死亡交叉)，並且我手上有股票，就「賣出」。

---

**`backtesting.py` 的程式碼:**

```python
class MovingAverageCross(Strategy):
    fast_ma_period = 10
    slow_ma_period = 30

    def init(self):
        self.fast_ma = self.I(SMA, self.data.Close, self.fast_ma_period)
        self.slow_ma = self.I(SMA, self.data.Close, self.slow_ma_period)

    def next(self):
        if not self.position and crossover(self.fast_ma, self.slow_ma):
            self.buy()
        elif self.position and crossover(self.slow_ma, self.fast_ma):
            self.sell()
```

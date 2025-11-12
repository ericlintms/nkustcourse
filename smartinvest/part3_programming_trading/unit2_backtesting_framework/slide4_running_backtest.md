# 投影片 4/4: 執行回測的流程

## 三步驟完成一個回測

```python
from backtesting import Backtest
# 假設 MyStrategy 和 my_data 都已經定義好了

# 1. 建立 Backtest 物件
#    - 第一個參數: 你的資料 (Pandas DataFrame)
#    - 第二個參數: 你的策略類別 (MyStrategy)
#    - 其他參數: 初始資金、手續費等
bt = Backtest(my_data, 
              MyStrategy, 
              cash=100000, 
              commission=.001425)

# 2. (可選) 執行參數最佳化
# stats = bt.optimize(ma_period=range(10, 30, 5))

# 3. 執行回測
stats = bt.run()

# 4. 查看結果
print(stats) # 在終端機印出績效摘要
bt.plot()    # 自動在瀏覽器中開啟詳細的互動式圖表
```

---

## 資料格式要求

* 必須是 Pandas DataFrame。
* Index 必須是 DatetimeIndex (時間序列)。
* 必須包含 `Open`, `High`, `Low`, `Close` 這四個欄位，且 **首字必須大寫**。
* 可以包含 `Volume` 欄位 (首字大寫)。

# 投影片 4/4: 參數最佳化 (Optimization)

**問題**: 我的 MA 策略，到底用 (10, 20) 好，還是 (12, 26) 好？我的 RSI 到底該用 14 天還是 20 天？

**參數最佳化**: 讓電腦幫我們測試所有可能的參數組合，並找出績效最好的一組。

---

**`backtesting.py` 的 `optimize` 方法**

```python
bt = Backtest(GOOG, MovingAverageCross, cash=10000)

# 告訴 optimize 要測試哪些參數的範圍
# fast_ma_period: 從 5 到 20，每隔 5 測試一次 (5, 10, 15, 20)
# slow_ma_period: 從 20 到 40，每隔 5 測試一次 (20, 25, 30, 35, 40)
stats = bt.optimize(
    fast_ma_period=range(5, 21, 5),
    slow_ma_period=range(20, 41, 5),
    # 告訴它以哪個指標作為最佳化的目標
    maximize='Sharpe Ratio' 
)

print("--- 最佳化結果 ---")
print(stats)

# 查看最佳參數
print("\n--- 最佳參數 ---")
print(stats._strategy)
```

---

## 過度最佳化的風險 (Overfitting)

* **警告**: 不要過度相信最佳化出來的「聖杯參數」。
* 一個在歷史數據上被過度「雕琢」的策略，很可能只是恰好符合過去的雜訊，而對未來完全無效。
* **建議**: 使用「樣本內 (In-Sample)」數據進行最佳化，並保留「樣本外 (Out-of-Sample)」數據來驗證最佳化後的策略是否依然有效。

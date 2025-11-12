# 單元 3: 策略實作與回測

本單元我們將動手把 Part 2 學到的擇時策略，用 `backtesting.py` 框架進行實作與回測。

## 學習目標

- 將移動平均線交叉策略寫成 `backtesting.py` 的 `Strategy`
- 將 RSI 超買超賣策略寫成 `Strategy`
- 執行回測並初步解讀結果

### 內容

1. **實作移動平均線交叉策略**
    - 定義快、慢兩條均線。
    - 在 `next()` 中使用 `crossover` 函式判斷黃金/死亡交叉。
    - 執行買入 (`self.buy()`) 和賣出 (`self.sell()`) 操作。
2. **實作 RSI 超買超賣策略**
    - 定義 RSI 指標。
    - 在 `next()` 中判斷 RSI 是否低於超賣區 (e.g., 30) 或高於超買區 (e.g., 70)。
    - 設定停損 (Stop Loss) 和停利 (Take Profit)。

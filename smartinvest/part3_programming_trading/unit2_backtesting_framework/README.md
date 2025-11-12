# 單元 2: 策略回測框架介紹

從零開始打造一個完整的回測系統非常複雜。幸運的是，有許多優秀的開源回測框架可以幫助我們。

## 學習目標

- 了解為什麼需要使用回測框架
- 認識 `backtesting.py` 這個輕量級的回測框架
- 學會 `backtesting.py` 的基本使用方法

### 內容

1. **為什麼要用框架？**
    - 自己寫回測系統的難點：資料處理、訂單管理、績效計算、繪圖...
    - 框架的好處：專注於策略邏輯，而非底層細節。
2. **`backtesting.py` 介紹**
    - 一個輕量、快速、易於上手的向量化回測框架。
    - 安裝： `pip install backtesting`
3. **`backtesting.py` 快速開始**
    - 準備 Pandas DataFrame 格式的資料 (欄位名稱須為 `Open`, `High`, `Low`, `Close`)。
    - 定義一個繼承 `backtesting.Strategy` 的策略類別。
    - 實作 `init()` 和 `next()` 方法。
    - 執行回測並印出結果。

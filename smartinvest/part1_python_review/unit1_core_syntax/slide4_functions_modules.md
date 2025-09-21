# 投影片 4/4: 函式與模組

## **函式 (Function): 可重複使用的程式碼區塊**

* **目的**: 避免重複撰寫相同的程式碼，讓程式更有組織。
* 使用 `def` 關鍵字來定義。

```python
def calculate_roi(buy_price, sell_price):
    return (sell_price - buy_price) / buy_price

# 呼叫函式
roi = calculate_roi(500, 600)
print(f"投資報酬率: {roi:.2%}") # 格式化輸出為百分比
```

---

## **模組 (Module): 功能的集合**

* **目的**: 將相關的函式、變數或類別組織在一個檔案中，方便管理和重複使用。
* 使用 `import` 來載入模組。

```python
# 載入 Python 內建的 math 模組
import math

print(math.sqrt(144)) # 計算平方根

# 載入第三方模組 (需要先安裝 pip install pandas)
import pandas as pd

df = pd.DataFrame(prices)
print(df.describe())
```

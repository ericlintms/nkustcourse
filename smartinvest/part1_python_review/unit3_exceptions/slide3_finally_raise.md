# 投影片 3/4: `finally` 與 `raise`

## `finally`: 無論如何都要執行

* 不管 `try` 區塊有沒有發生錯誤，`finally` 區塊裡的程式碼 **永遠** 會被執行。
* **用途**: 常用於資源的釋放，例如關閉檔案、關閉網路連線等，確保程式不會留下後遺症。

```python
f = None # 先宣告變數
try:
    f = open("my_data.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("檔案不存在！")
finally:
    if f:
        f.close() # 確保檔案一定會被關閉
        print("檔案已關閉")
```

---

## `raise`: 主動引發錯誤

* 有時候，我們需要根據業務邏輯自己創造錯誤。

```python
def withdraw(amount):
    if amount > my_balance:
        # 主動引發一個 ValueError
        raise ValueError("餘額不足！")
    # ... (執行提款)

try:
    withdraw(50000)
except ValueError as e:
    print(f"提款失敗: {e}")
```

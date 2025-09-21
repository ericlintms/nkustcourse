# 投影片 4/4: 自訂例外 (Custom Exceptions)

## 為什麼要自訂例外？

Python 內建的例外 (如 `ValueError`, `TypeError`) 有時候無法精確描述我們應用程式中發生的特定錯誤。

自訂例外可以讓我們的錯誤處理更有語意、更清晰。

---

## 如何建立？

* 建立一個新的 Class，讓它繼承自 `Exception` 或其他內建的例外類別。

```python
# 建立一個我們自己 App 的基礎例外
class TradingAppError(Exception):
    pass

# 建立一個更具體的例外，繼承自我們自己的基礎例外
class InsufficientFundsError(TradingAppError):
    """當帳戶資金不足時引發"""
    def __init__(self, required, balance):
        self.message = f"資金不足，需要 {required} 但只有 {balance}"
        super().__init__(self.message)

def buy_stock(cost):
    if cost > my_balance:
        raise InsufficientFundsError(cost, my_balance)

try:
    buy_stock(10000)
except InsufficientFundsError as e:
    # 我們可以很清楚地知道這是「資金不足」的錯誤
    print(f"交易錯誤: {e}")
```
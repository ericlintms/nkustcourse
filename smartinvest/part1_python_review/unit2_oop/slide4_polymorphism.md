# 投影片 4/4: 多型 (Polymorphism)

## 字面意義:「多種型態」

* 不同的物件，即使是不同的類別，只要有相同名稱的方法，就可以用同樣的方式來對待它們。
* **目的**: 讓程式碼更有彈性、更容易擴充。

---

## 範例: 投資組合報告

```python
class Stock:
    # ... (省略)
    def display(self):
        print(f"[股票] {self.name}")

class Bond:
    # ... (省略)
    def display(self):
        print(f"[債券] {self.name}")

# --- 重點 --- #
# 這個函式不管傳進來的是 Stock 還是 Bond，
# 只要它有 .display() 方法，就能正常運作！
def generate_report(instrument):
    instrument.display()

stock = Stock("台積電", "2330")
bond = Bond("公司債A")

portfolio = [stock, bond]

for item in portfolio:
    generate_report(item) # 同一個函式，處理不同型態的物件
```

## 好處

未來如果新增一個 `class Fund(FinancialInstrument)`，只要它也有 `display` 方法，`generate_report` 函式完全不需要修改！

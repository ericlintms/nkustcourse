# 投影片 3/4: 繼承 (Inheritance)

## 目的: 程式碼的重複使用與擴充

當不同的 Class 有共同的屬性或方法時，我們可以將共通的部分抽出來，建立一個「父類別」。

其他的「子類別」可以「繼承」這個父類別，直接擁有父類別的所有功能，並且可以加上自己特有的功能。

---

## 範例: 金融商品

```python
# 父類別: 所有金融商品的共通點
class FinancialInstrument:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"商品名稱: {self.name}")

# 子類別: 股票繼承了金融商品
class Stock(FinancialInstrument):
    # 擴充自己的屬性
    def __init__(self, name, stock_id):
        super().__init__(name) # 呼叫父類別的 init
        self.stock_id = stock_id

    # 擴充自己的方法
    def show_id(self):
        print(f"股票代號: {self.stock_id}")

# 子類別: 債券也繼承了金融商品
class Bond(FinancialInstrument):
    pass # 暫時沒有新功能


stock = Stock("台積電", "2330")
stock.show_name() # 從父類別繼承來的方法
stock.show_id()   # 自己的方法
```

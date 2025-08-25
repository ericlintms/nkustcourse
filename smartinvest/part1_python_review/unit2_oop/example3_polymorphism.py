# 範例 3: 多型 (Polymorphism)

# 承襲 example2_inheritance.py 的 Class 定義
class FinancialInstrument:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        raise NotImplementedError("子類別必須實作這個方法")

class Stock(FinancialInstrument):
    def __init__(self, name, stock_id, price):
        super().__init__(name, price)
        self.stock_id = stock_id

    def display_info(self):
        print(f"[股票] {self.name} ({self.stock_id}), 價格: {self.price}")

class Bond(FinancialInstrument):
    def __init__(self, name, price, interest_rate):
        super().__init__(name, price)
        self.interest_rate = interest_rate

    def display_info(self):
        print(f"[債券] {self.name}, 價格: {self.price}, 利率: {self.interest_rate}%")

# 雖然 stock 和 bond 是不同類型的物件，但我們可以用同樣的方式與它們互動
def print_instrument_info(instrument):
    instrument.display_info()

stock = Stock("台積電", "2330", 600)
bond = Bond("公司債A", 1000, 3.5)

# 同一個函式可以接受不同類型的物件
print_instrument_info(stock)
print_instrument_info(bond)

# 也可以用一個 list 來管理它們
portfolio = [stock, bond]
print("\n--- 投資組合 ---")
for item in portfolio:
    item.display_info()

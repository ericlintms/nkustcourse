# 範例 2: 繼承 (Inheritance)

# 定義一個基礎的金融商品 Class
class FinancialInstrument:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_value(self):
        return self.price

# Stock (股票) Class 繼承自 FinancialInstrument
class Stock(FinancialInstrument):
    def __init__(self, name, stock_id, price):
        # 呼叫父類別的建構函式
        super().__init__(name, price)
        self.stock_id = stock_id

    def display_info(self):
        print(f"{self.name} ({self.stock_id}) 的價值為 {self.get_value()}")

# Bond (債券) Class 也繼承自 FinancialInstrument
class Bond(FinancialInstrument):
    def __init__(self, name, interest_rate):
        super().__init__(name, 1000) # 假設債券面額固定為 1000
        self.interest_rate = interest_rate

    def display_info(self):
        print(f"{self.name} 的價值為 {self.get_value()}，年利率為 {self.interest_rate}%")


stock = Stock("台積電", "2330", 600)
bond = Bond("美國十年期公債", 1.5)

stock.display_info()
bond.display_info()

# 範例 1: Class 與 Object

class Stock:
    # 建構函式: 當一個物件被建立時會自動呼叫
    def __init__(self, name, stock_id, price):
        self.name = name
        self.stock_id = stock_id
        self.price = price

    # 物件的方法 (method)
    def display_info(self):
        print(f"股票名稱: {self.name}")
        print(f"股票代號: {self.stock_id}")
        print(f"目前價格: {self.price}")

# 建立一個 Stock 物件 (instance)
stock1 = Stock("台積電", "2330", 600)
stock2 = Stock("聯發科", "2454", 900)

# 呼叫物件的方法
stock1.display_info()
print("---")
stock2.display_info()

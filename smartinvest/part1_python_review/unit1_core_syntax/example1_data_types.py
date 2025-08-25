# 範例 1: 資料型態與資料結構

# 數字 (Integer, Float)
price = 120.5
quantity = 3
total_price = price * quantity
print(f"股票價格: {price}, 數量: {quantity}, 總價: {total_price}")

# 字串 (String)
stock_name = "台積電"
stock_id = "2330"
print(stock_name + " (" + stock_id + ")")

# 列表 (List) - 常用於儲存一系列有序的資料
prices = [120.5, 121.0, 120.0, 122.5]
print(f"歷史價格: {prices}")
print(f"第一天的價格: {prices[0]}")

# 字典 (Dictionary) - 常用於儲存鍵值對 (key-value) 資料
stock_info = {
    "name": "台積電",
    "id": "2330",
    "price": 120.5
}
print(f"股票資訊: {stock_info}")
print(f"股票名稱: {stock_info['name']}")

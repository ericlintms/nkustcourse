# 範例: 純 Python 的策略邏輯

# 在使用任何框架之前，我們先用最單純的 Python 來思考策略是怎麼一回事。
# 假設這是一段歷史收盤價
prices = [100, 102, 105, 103, 101, 99, 102, 106, 108, 105]

# 我們的簡單策略：如果價格連續兩天上涨，就買入；如果連續兩天下跌，就賣出。

# 持有部位狀態 (True 代表持有，False 代表空手)
position = False

# 用 for 迴圈遍歷價格，從第三天開始 (因為需要前兩天的資料來比較)
for i in range(2, len(prices)):
    current_price = prices[i]
    prev_price_1 = prices[i-1]
    prev_price_2 = prices[i-2]
    
    print(f"日期 {i+1}: 價格 {current_price}")

    # --- 買入條件 ---
    # 如果價格連續兩天上涨，且我們目前沒有部位
    if current_price > prev_price_1 and prev_price_1 > prev_price_2 and not position:
        print(f"  -> 訊號: 連續上漲，執行買入！")
        position = True
        
    # --- 賣出條件 ---
    # 如果價格連續兩天下跌，且我們目前持有部位
    elif current_price < prev_price_1 and prev_price_1 < prev_price_2 and position:
        print(f"  -> 訊號: 連續下跌，執行賣出！")
        position = False
    else:
        print("  -> 訊號: 無，繼續觀察")

print(f"\n回測結束，最終持有狀態: {'持有部位' if position else '空手'}")

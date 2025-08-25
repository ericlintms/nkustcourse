# 範例 2: 流程控制

# if/elif/else
price = 121.0

if price > 120.0:
    print("價格高於 120，考慮賣出")
elif price < 110.0:
    print("價格低於 110，考慮買入")
else:
    print("價格在正常範圍，繼續觀察")

# for 迴圈 - 迭代一個序列
prices = [120.5, 121.0, 120.0, 122.5]
for p in prices:
    print(f"今日價格: {p}")

# while 迴圈 - 當條件成立時重複執行
count = 0
while count < 3:
    print(f"第 {count + 1} 次檢查價格...")
    count += 1

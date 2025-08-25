# 範例 1: 繪製折線圖與長條圖

import pandas as pd
import matplotlib.pyplot as plt

# 準備資料
data = {
    'Price': [600, 605, 602, 610, 608],
    'Volume': [50000, 55000, 48000, 60000, 52000]
}
index = pd.to_datetime(['2023-10-01', '2023-10-02', '2023-10-03', '2023-10-04', '2023-10-05'])
df = pd.DataFrame(data, index=index)

# --- 繪製收盤價折線圖 ---
plt.figure(figsize=(10, 5)) # 設定圖表大小
plt.plot(df.index, df['Price'])
plt.title('Stock Price Over Time') # 設定標題
plt.xlabel('Date') # 設定 X 軸標籤
plt.ylabel('Price') # 設定 Y 軸標籤
plt.grid(True) # 顯示格線
plt.show() # 顯示圖表

# --- 繪製成交量長條圖 ---
plt.figure(figsize=(10, 5))
plt.bar(df.index, df['Volume'], color='skyblue')
plt.title('Trading Volume Over Time')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.show()

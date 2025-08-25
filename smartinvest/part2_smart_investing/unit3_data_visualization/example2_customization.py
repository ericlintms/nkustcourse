# 範例 2: 圖表客製化與多重序列

import pandas as pd
import matplotlib.pyplot as plt

# 準備資料，包含兩支股票
data = {
    'Stock_A_Price': [100, 102, 101, 105, 107],
    'Stock_B_Price': [50, 51, 52, 51, 53]
}
index = pd.to_datetime(['2023-10-01', '2023-10-02', '2023-10-03', '2023-10-04', '2023-10-05'])
df = pd.DataFrame(data, index=index)

# 計算 3 日移動平均線
df['Stock_A_MA3'] = df['Stock_A_Price'].rolling(window=3).mean()

plt.figure(figsize=(12, 6))

# 繪製 A 股票的價格
plt.plot(df.index, df['Stock_A_Price'], 
         color='blue', 
         linestyle='-', 
         marker='o', 
         label='Stock A Price')

# 繪製 A 股票的 3 日移動平均線
plt.plot(df.index, df['Stock_A_MA3'],
         color='orange',
         linestyle='--',
         label='Stock A 3-Day MA')

# 繪製 B 股票的價格
# plt.plot(df.index, df['Stock_B_Price'], color='green', label='Stock B Price')

# --- 客製化 ---
plt.title('Stock Prices and Moving Average', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Price', fontsize=12)
plt.legend() # 顯示圖例
plt.grid(True)

plt.show()

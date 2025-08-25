# 範例 1: 移動平均線 (Moving Average)

import pandas as pd
import matplotlib.pyplot as plt

# 準備股價資料
data = {
    'Close': [100, 102, 101, 105, 107, 106, 108, 110, 112, 109, 107, 105, 103, 106, 108]
}
index = pd.to_datetime(pd.date_range(start='2023-10-01', periods=15))
df = pd.DataFrame(data, index=index)

# --- 計算移動平均線 (MA) ---
# 使用 .rolling(window=N) 來指定計算期間
# .mean() 來計算平均值
df['MA5'] = df['Close'].rolling(window=5).mean() # 5日均線 (短線)
df['MA10'] = df['Close'].rolling(window=10).mean() # 10日均線 (長線)

print("--- 股價與移動平均線 ---")
print(df.tail())

# --- 繪圖觀察 ---
plt.figure(figsize=(12, 6))
plt.plot(df['Close'], label='Close Price', color='black')
plt.plot(df['MA5'], label='5-Day MA', color='blue', linestyle='--')
plt.plot(df['MA10'], label='10-Day MA', color='red', linestyle='--')

plt.title('Moving Average (MA) Strategy')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()

# 在這個例子中，我們可以看到在圖表後段，藍色的短期均線(MA5)向下跌破紅色的長期均線(MA10)
# 這就是一個「死亡交叉」的賣出訊號。

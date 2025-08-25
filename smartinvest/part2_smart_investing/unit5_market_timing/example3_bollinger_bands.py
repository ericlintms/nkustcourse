# 範例 3: 布林通道 (Bollinger Bands)

import pandas as pd
import matplotlib.pyplot as plt

# 準備股價資料
data = {
    'Close': [100, 102, 101, 105, 107, 106, 108, 110, 112, 109, 107, 105, 103, 106, 108, 105, 103, 100, 98, 96]
}
index = pd.to_datetime(pd.date_range(start='2023-10-01', periods=20))
df = pd.DataFrame(data, index=index)

# --- 計算布林通道 --- #
window = 10 # 使用 10 日的移動平均
std_dev_multiplier = 2 # 使用 2 倍標準差

# 1. 中軌: N日的移動平均線
df['BB_Mid'] = df['Close'].rolling(window=window).mean()

# 2. 計算 N 日的標準差
df['BB_Std'] = df['Close'].rolling(window=window).std()

# 3. 上軌: 中軌 + (標準差 * K)
df['BB_Upper'] = df['BB_Mid'] + (df['BB_Std'] * std_dev_multiplier)

# 4. 下軌: 中軌 - (標準差 * K)
df['BB_Lower'] = df['BB_Mid'] - (df['BB_Std'] * std_dev_multiplier)

print("--- 布林通道數據 ---")
print(df.tail())

# --- 繪圖觀察 ---
plt.figure(figsize=(12, 6))
plt.plot(df['Close'], label='Close Price', color='black')
plt.plot(df['BB_Mid'], label=f'{window}-Day MA', color='blue', linestyle='--')
plt.plot(df['BB_Upper'], label='Upper Band', color='red', linestyle=':')
plt.plot(df['BB_Lower'], label='Lower Band', color='green', linestyle=':')

# 使用 fill_between 來填充上下軌之間的區域
plt.fill_between(df.index, df['BB_Upper'], df['BB_Lower'], color='gray', alpha=0.2)

plt.title('Bollinger Bands')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()

# 在圖表後段，價格觸及並跌破了下軌，這可能是一個超賣訊號，暗示著可能的反彈。

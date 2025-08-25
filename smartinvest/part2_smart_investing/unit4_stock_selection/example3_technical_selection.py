# 範例 3: 技術指標選股 (RSI)

import pandas as pd

# 假設我們有一個包含多支股票收盤價的 DataFrame
# 在實務中，這需要迴圈或函式來計算每支股票的 RSI
data = {
    'Stock_A': [100, 98, 95, 93, 96, 98, 100],
    'Stock_B': [50, 55, 60, 58, 57, 55, 52],
    'Stock_C': [200, 190, 180, 175, 170, 168, 165] # 一路下跌
}
df = pd.DataFrame(data)

# --- 計算 RSI 的簡化函式 ---
def calculate_rsi(prices, period=14):
    delta = prices.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

# --- 對每一支股票計算 RSI ---
rsi_results = {}
for stock_name in df.columns:
    rsi = calculate_rsi(df[stock_name], period=5) # 為了示範，用較短的週期
    rsi_results[stock_name] = rsi.iloc[-1] # 取得最新的 RSI 值

print("--- 最新 RSI 值 ---")
for stock, rsi_value in rsi_results.items():
    print(f"{stock}: {rsi_value:.2f}")

# --- 篩選出 RSI < 30 (超賣區) 的股票 ---
oversold_stocks = []
for stock, rsi_value in rsi_results.items():
    if rsi_value < 30:
        oversold_stocks.append(stock)

print("\n--- 進入超賣區，可能出現反彈機會的股票 ---")
if oversold_stocks:
    print(oversold_stocks)
else:
    print("無")

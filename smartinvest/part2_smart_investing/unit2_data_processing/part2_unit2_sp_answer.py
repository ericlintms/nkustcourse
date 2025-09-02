import pandas as pd

# 原始資料
data = {
    'Ticker': ['AAPL', 'MSFT', 'GOOGL', 'AMZN'],
    'Price': [170, 300, 135, 140],
    'SharesOutstanding': [15.5e9, 7.4e9, 12.7e9, 10.1e9]
}

# 1. 建立 DataFrame
df = pd.DataFrame(data)
print("--- 原始 DataFrame ---")
print(df)

# 2. 篩選出 Price > 150 的股票
high_price_stocks = df[df['Price'] > 150]
print("\n--- Price > 150 的股票 ---")
print(high_price_stocks)

# 3. 計算並新增 MarketCap 欄位
df['MarketCap'] = df['Price'] * df['SharesOutstanding']
print("\n--- 包含 MarketCap 的 DataFrame ---")
print(df)

# 要執行此腳本，請先安裝 pandas:
# pip install pandas

# 範例 1: 價值投資選股

import pandas as pd

# 假設我們有包含多家公司基本面數據的 DataFrame
# 在實務中，這些數據需要從財經資料庫或爬蟲取得
data = {
    'StockID': ['2330', '2454', '2317', '1301', '2881'],
    'Name': ['台積電', '聯發科', '鴻海', '台塑', '富邦金'],
    'PE_Ratio': [20.5, 25.1, 15.3, 18.2, 8.5], # 本益比
    'PB_Ratio': [5.8, 4.2, 1.2, 1.0, 1.1], # 股價淨值比
    'Dividend_Yield': [2.5, 3.1, 4.5, 5.2, 6.1] # 股息殖利率 (%)
}
df = pd.DataFrame(data)

print("--- 原始股票池 ---")
print(df)

# --- 設定價值投資的篩選條件 ---
# 1. 本益比 (PE Ratio) < 20
# 2. 股價淨值比 (PB Ratio) < 1.5
# 3. 股息殖利率 (Dividend Yield) > 4%

condition_pe = df['PE_Ratio'] < 20
condition_pb = df['PB_Ratio'] < 1.5
condition_yield = df['Dividend_Yield'] > 4

# 將所有條件用 & (AND) 組合起來
value_stocks = df[condition_pe & condition_pb & condition_yield]

print("\n--- 符合價值投資條件的股票 ---")
print(value_stocks)

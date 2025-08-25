# 範例 3: 資料選取與過濾

import pandas as pd

# 假設我們從 CSV 檔案讀取資料
# 先建立一個假的 CSV 檔
csv_content = """
Date,StockID,Open,High,Low,Close,Volume
2023-10-01,2330,600,605,598,605,50000
2023-10-02,2330,606,610,605,610,55000
2023-10-01,2454,900,910,895,910,30000
2023-10-02,2454,911,915,908,912,32000
2023-10-03,2330,610,610,602,603,48000
"""
with open('dummy_stocks.csv', 'w') as f:
    f.write(csv_content)

# 從 CSV 讀取資料，並將 Date 欄位設為索引
df = pd.read_csv('dummy_stocks.csv', index_col='Date', parse_dates=True)

print("--- 原始資料 ---")
print(df)

# --- 條件過濾 --- #

# 1. 找出 StockID 是 2330 的所有資料
df_2330 = df[df['StockID'] == 2330]
print("\n--- 只看 2330 (台積電) ---")
print(df_2330)

# 2. 找出收盤價 (Close) 高於 605 的資料
high_close_df = df[df['Close'] > 605]
print("\n--- 收盤價 > 605 ---")
print(high_close_df)

# 3. 找出成交量 (Volume) 大於 50000 且 StockID 是 2330 的資料
complex_filter_df = df[(df['Volume'] > 50000) & (df['StockID'] == 2330)]
print("\n--- 台積電且成交量 > 50000 ---")
print(complex_filter_df)

# --- 新增欄位 --- #
# 計算當日振幅 (High - Low)
df['Amplitude'] = df['High'] - df['Low']
print("\n--- 新增振幅欄位 ---")
print(df)

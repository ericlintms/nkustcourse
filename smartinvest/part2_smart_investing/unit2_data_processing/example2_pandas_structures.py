# 範例 2: Pandas DataFrame 與 Series

import pandas as pd

# --- Series: 一維帶有索引的資料 --- #
# 就像是字典，但更強大
stock_prices = pd.Series([600, 605, 602], index=['2023-10-01', '2023-10-02', '2023-10-03'])
print("--- Stock Prices (Series) ---")
print(stock_prices)
print(f"\n10月2日的價格: {stock_prices['2023-10-02']}")


# --- DataFrame: 二維表格資料 --- #
# 這是我們最常用的資料結構
data = {
    'Price': [600, 605, 602, 610, 608],
    'Volume': [50000, 55000, 48000, 60000, 52000]
}
index = pd.to_datetime(['2023-10-01', '2023-10-02', '2023-10-03', '2023-10-04', '2023-10-05'])

df = pd.DataFrame(data, index=index)

print("\n--- Stock Data (DataFrame) ---")
print(df)

# --- 基本操作 ---
# 取得欄位 (Column)
prices_col = df['Price']
print("\n--- Price Column (a Series) ---")
print(prices_col)

# 取得列 (Row) - 使用 .loc
row_by_date = df.loc['2023-10-03']
print("\n--- Row for 2023-10-03 ---")
print(row_by_date)

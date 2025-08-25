# 範例 2: 成長股投資選股

import pandas as pd

# 假設我們有包含多家公司成長性數據的 DataFrame
data = {
    'StockID': ['2330', '2454', '6415', '1301', '3008'],
    'Name': ['台積電', '聯發科', '矽力杰', '台塑', '大立光'],
    'Revenue_Growth_YoY': [15.2, 25.8, 30.1, -5.4, 10.5], # 年營收成長率 (%)
    'EPS_Growth_YoY': [18.3, 28.9, 35.2, -8.1, 12.3], # 年每股盈餘成長率 (%)
    'Gross_Margin': [52.3, 48.1, 55.4, 15.2, 60.1] # 毛利率 (%)
}
df = pd.DataFrame(data)

print("--- 原始股票池 ---")
print(df)

# --- 設定成長股投資的篩選條件 ---
# 1. 年營收成長率 > 20%
# 2. 年 EPS 成長率 > 20%
# 3. 毛利率 > 50%

condition_rev_growth = df['Revenue_Growth_YoY'] > 20
condition_eps_growth = df['EPS_Growth_YoY'] > 20
condition_margin = df['Gross_Margin'] > 50

growth_stocks = df[condition_rev_growth & condition_eps_growth & condition_margin]

print("\n--- 符合成長股投資條件的股票 ---")
print(growth_stocks)

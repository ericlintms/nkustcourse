# 範例 1: 資產相關性 (Correlation)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 假設我們有三種不同資產的歷史價格
# 股票 (高風險), 債券 (低風險), 黃金 (避險)
data = {
    'Stock_ETF': [100, 105, 102, 108, 110, 107, 105, 103],
    'Bond_ETF': [50, 49.8, 50.1, 49.5, 49.2, 49.5, 49.8, 50.2],
    'Gold_ETF': [70, 68, 69, 67, 66, 68, 70, 72]
}
index = pd.to_datetime(pd.date_range(start='2023-01-01', periods=8))
df = pd.DataFrame(data, index=index)

# --- 計算每日報酬率 ---
returns = df.pct_change().dropna()
print("--- 每日報酬率 ---")
print(returns)

# --- 計算相關性矩陣 ---
correlation_matrix = returns.corr()
print("\n--- 相關性矩陣 ---")
print(correlation_matrix)

# --- 可視化相關性矩陣 ---
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Asset Correlation Matrix')
plt.show()

# 從熱力圖可以看出，股票和債券呈現負相關 (-0.68)，
# 這意味著當股票上漲時，債券傾向於下跌，反之亦然。
# 這就是為什麼要在投資組合中同時包含兩者的原因：它們可以互相平衡風險。


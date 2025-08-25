# 範例 2: 投資組合報酬率

import pandas as pd

# 假設的資產歷史報酬率 (單位: %)
data = {
    'Stock_Returns': [15, 20, -10, 25, -5],
    'Bond_Returns': [3, 2, 2.5, 1.5, 4]
}
df = pd.DataFrame(data)

# --- 設定投資組合權重 ---
# 股債比 60/40
weights = {
    'Stock': 0.6,
    'Bond': 0.4
}

# --- 計算投資組合的年度報酬率 ---
# 投資組合報酬率 = (股票報酬率 * 股票權重) + (債券報酬率 * 債券權重)
df['Portfolio_Returns'] = (df['Stock_Returns'] * weights['Stock']) + (df['Bond_Returns'] * weights['Bond'])

print("--- 投資組合報酬率計算 ---")
print(df)

# --- 比較績效 ---
average_stock_return = df['Stock_Returns'].mean()
average_bond_return = df['Bond_Returns'].mean()
average_portfolio_return = df['Portfolio_Returns'].mean()

print(f"\n平均股票報酬: {average_stock_return:.2f}%")
print(f"平均債券報酬: {average_bond_return:.2f}%")
print(f"平均投資組合報酬: {average_portfolio_return:.2f}%")

# --- 比較風險 (用標準差衡量) ---
std_stock = df['Stock_Returns'].std()
std_bond = df['Bond_Returns'].std()
std_portfolio = df['Portfolio_Returns'].std()

print(f"\n股票風險 (標準差): {std_stock:.2f}")
print(f"債券風險 (標準差): {std_bond:.2f}")
print(f"投資組合風險 (標準差): {std_portfolio:.2f}")

# 可以看到，投資組合的風險顯著低於單純持有股票，但報酬率又高於單純持有債券。
# 這就是資產配置的力量。

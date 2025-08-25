# 範例 3: 手動計算最大回撤 (Max Drawdown)

import pandas as pd

# 假設這是我們的資金曲線 (Equity Curve)
equity_curve = pd.Series([10000, 10500, 10200, 10800, 11000, 10700, 10300, 9800, 10100, 11200, 11500, 11300])

# 1. 計算歷史最高點 (Cumulative Maximum)
# .cummax() 會計算到目前為止的序列最大值
cumulative_max = equity_curve.cummax()

# 2. 計算每日的回撤 (Drawdown)
# 回撤 = (目前價值 - 歷史最高點) / 歷史最高點
drawdown = (equity_curve - cumulative_max) / cumulative_max

# 3. 找出最大的回撤值
max_drawdown = drawdown.min()

# --- 將過程可視化 ---
results = pd.DataFrame({
    'Equity': equity_curve,
    'Peak': cumulative_max,
    'Drawdown_Percent': drawdown * 100
})

print("--- 最大回撤計算過程 ---")
print(results)

print(f"\n最大回撤 (Max Drawdown): {max_drawdown:.2%}")

# 從表格中可以看到，在第 8 個時間點，資金從最高點 11000 跌到 9800，
# 產生了 -10.91% 的最大回撤。

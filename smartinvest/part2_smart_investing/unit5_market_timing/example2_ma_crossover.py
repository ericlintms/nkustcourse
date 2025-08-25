# 範例 2: 移動平均線交叉策略訊號

import pandas as pd

# 承接範例1的資料
data = {
    'Close': [100, 102, 101, 105, 107, 106, 108, 110, 112, 109, 107, 105, 103, 106, 108]
}
index = pd.to_datetime(pd.date_range(start='2023-10-01', periods=15))
df = pd.DataFrame(data, index=index)

df['MA5'] = df['Close'].rolling(window=5).mean()
df['MA10'] = df['Close'].rolling(window=10).mean()

# --- 產生交易訊號 --- #

# 1. 找出 MA5 > MA10 的日子 (黃金交叉或多頭排列)
df['MA5_gt_MA10'] = (df['MA5'] > df['MA10']).astype(bool)


# 2. 找出「昨天 MA5 <= MA10」但「今天 MA5 > MA10」的日子，這就是黃金交叉點
prev_ma5_gt_ma10 = df['MA5_gt_MA10'].shift(1).infer_objects(copy=False).astype(bool)
df['Golden_Cross'] = df['MA5_gt_MA10'] & (~prev_ma5_gt_ma10)

# 3. 找出「死亡交叉」點
df['Death_Cross'] = (~df['MA5_gt_MA10']) & prev_ma5_gt_ma10


print("--- 交叉訊號 ---")
# 只顯示有發生交叉訊號的日子
signals = df[df['Golden_Cross'] | df['Death_Cross']]
print(signals)

# 從結果可以看到，在 2023-10-12 發生了死亡交叉

# 投影片 4/4: 條件過濾與新增欄位

## 讓 DataFrame 幫你找出符合條件的資料

---

### 布林過濾 (Boolean Filtering)

核心觀念: `df[...]` 中括號裡可以放一個「布林值的 Series」。

```python
# 步驟 1: 產生一個布林值的 Series
# (收盤價 > 600 的日子會是 True，反之為 False)
condition = df['Close'] > 600

# 步驟 2: 將這個 Series 丟回 df
# DataFrame 會只保留 condition 中為 True 的那些列
high_price_days = df[condition]

# --- 合併成一行 --- #
high_price_days = df[df['Close'] > 600]
```

### 多重條件

* `&`: AND (而且)
* `|`: OR (或者)

```python
# 收盤價 > 600 **而且** 成交量 > 50000
condition = (df['Close'] > 600) & (df['Volume'] > 50000)
result = df[condition]
```

---

## 新增/修改欄位

就像操作字典一樣簡單！

```python
# 新增一個叫 'DailyChange' 的欄位
df['DailyChange'] = df['Close'] - df['Open']
```
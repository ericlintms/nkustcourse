# 投影片 3/4: 選取你想要的資料 (Slicing & Dicing)

## 從 DataFrame 中拿出需要的部份

---

### 1. 選取「欄」 (Columns)

```python
# 選取單一欄位 (結果會是一個 Series)
close_prices = df['Close']

# 選取多個欄位 (結果會是一個新的 DataFrame)
ohlc = df[['Open', 'High', 'Low', 'Close']]
```

---

### 2. 選取「列」 (Rows)

* **`.loc`**: 使用「標籤 (Label)」來選取 (例如日期)
* **`.iloc`**: 使用「位置 (Integer Position)」來選取 (例如第 0, 1, 2 筆)

```python
# .loc: 取得 2023年10月10日的資料
day_data = df.loc['2023-10-10']

# .loc: 取得 2023年10月的所有資料
month_data = df.loc['2023-10']

# .iloc: 取得第一筆資料 (位置 0)
first_day = df.iloc[0]

# .iloc: 取得前 5 筆資料
first_5_days = df.iloc[0:5]
```
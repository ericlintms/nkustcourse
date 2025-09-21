# 投影片 2/4: 讀寫 CSV 檔案

## CSV: 表格資料的好朋友

```csv
Date,Open,High,Low,Close
2023-10-01,120,122,119,121
2023-10-02,121,123,120,122
```

Python 內建 `csv` 模組，讓處理 CSV 變得很簡單。

---

## 寫入 CSV

```python
import csv

# 準備要寫入的資料 (list of lists)
data = [
    ['Date', 'Open', 'Close'],
    ['2023-10-01', 120, 121],
]

with open('prices.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)
```

---

## 讀取 CSV

```python
with open('prices.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```
# 投影片 2/4: Pandas 核心 - DataFrame

## DataFrame: 你的智慧型 Excel 表格

DataFrame 是一個二維的、帶有標籤的資料結構，你可以把它想像成一個 Excel 工作表或資料庫的表格。

![DataFrame](https://storage.googleapis.com/gweb-cloud-media/notebook-training-images/pandas-dataframe.png)

---

## DataFrame 的組成

* **Index (索引)**: 列的標籤，在金融數據中通常是 **日期**。
* **Columns (欄)**: 欄的標籤，代表不同的數據維度 (e.g., `Open`, `High`, `Low`, `Close`, `Volume`)。
* **Data (資料)**: 實際的數值，底層由 NumPy 陣列支撐，所以運算速度很快。

---

## 如何建立 DataFrame

最常見的方式是從檔案讀取：

```python
import pandas as pd

# 從 CSV 檔案讀取，並將 'Date' 欄位作為 Index
df = pd.read_csv('stock_2330.csv', 
                 index_col='Date', 
                 parse_dates=True)

print(df.head()) # .head() 可以看前五筆資料
```
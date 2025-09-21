# 投影片 3/4: 讀寫 JSON 檔案

## JSON: 彈性、易讀的資料格式

* 由「鍵值對」組成，類似 Python 的字典。
* 可以有巢狀結構。

```json
{
    "stock_id": "2330",
    "stock_name": "台積電",
    "history_prices": [
        {"date": "2023-10-01", "price": 600},
        {"date": "2023-10-02", "price": 605}
    ]
}
```

---

## 寫入 JSON (Python 物件 -> JSON 字串)

```python
import json

# 準備一個 Python 字典
data = {"stock_id": "2330", "stock_name": "台積電"}

with open('stock.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
```

---

## 讀取 JSON (JSON 字串 -> Python 物件)

```python
with open('stock.json', 'r', encoding='utf-8') as f:
    stock_data = json.load(f)
    print(stock_data['stock_name'])
```
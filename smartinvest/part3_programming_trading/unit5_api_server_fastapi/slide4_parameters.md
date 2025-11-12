# 投影片 4/4: 路徑與查詢參數

## 如何讓 API 接收外部傳入的資料？

---

### 1. 路徑參數 (Path Parameters)

* 將參數值作為路徑的一部分。
* **用途**: 用來指定一個特定的「資源」。
* **語法**: 在路徑中使用大括號 `{}`，並在函式中定義同名的參數。

```python
# URL: /stocks/2330
@app.get("/stocks/{stock_id}")
def get_stock_info(stock_id: str):
    # stock_id 的值會是 "2330"
    return {"info_for": stock_id}
```

---

### 2. 查詢參數 (Query Parameters)

* 附加在 URL 的 `?` 後面，由 `key=value` 組成，多個參數用 `&` 分隔。
* **用途**: 用來對結果進行過濾、排序或分頁。
* **語法**: 在函式中定義「沒有出現在路徑中」的參數。

```python
# URL: /search?keyword=apple&limit=5
@app.get("/search")
def search_items(keyword: str, limit: int = 10):
    # keyword 的值是 "apple"
    # limit 的值是 5 (如果沒給，預設是 10)
    return {"searching": keyword, "max_results": limit}
```

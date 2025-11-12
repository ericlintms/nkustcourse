# 投影片 3/4: FastAPI 的 Hello World

## 三行程式碼，啟動一個 API 伺服器

```python
# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}
```

---

## 程式碼解析

1. `app = FastAPI()`: 建立一個 FastAPI 的主體實例。

2. `@app.get("/")`: **路徑操作裝飾器 (Path Operation Decorator)**
    * `@`: 這是 Python 的裝飾器語法。
    * `get`: 指的是 HTTP 的 GET 方法 (通常用於讀取資料)。
    * `"/"`: 指的是 API 的路徑 (Path)。根路徑就是網站首頁。

3. `def read_root(): ...`: **路徑操作函式 (Path Operation Function)**
    * 當有請求送到 `/` 這個路徑時，FastAPI 就會呼叫這個函式。
    * 函式回傳的 Python 字典或列表，會被 FastAPI 自動轉換成 JSON 格式。

---

**如何執行？**

在終端機執行：
`uvicorn main:app --reload`

* `main`: 指的是 `main.py` 這個檔案。
* `app`: 指的是檔案中 `app = FastAPI()` 這個物件。
* `--reload`: 讓伺服器在程式碼變更後自動重啟，開發時非常方便。

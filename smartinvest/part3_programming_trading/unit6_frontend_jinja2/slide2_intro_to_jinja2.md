# 投影片 2/4: Jinja2 介紹與設定

## Jinja2: Python 最流行的模板引擎之一

* 由 `Flask` 的作者開發，語法靈感來自 Django 模板。
* 功能強大、速度快、安全性高。
* FastAPI 官方推薦的模板引擎之一。

---

## 在 FastAPI 中設定 Jinja2

### 1. 安裝

```bash
pip install jinja2
```

**2. 建立 `templates` 目錄**

按照慣例，我們會將所有的 HTML 模板檔案放在一個名為 `templates` 的資料夾中。

### 3. 在 Python 中設定

```python
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

app = FastAPI()

# 建立一個 Jinja2Templates 實例，並告訴它模板在哪裡
templates = Jinja2Templates(directory="templates")
```

**4. 在路徑函式中回傳 `TemplateResponse`**

```python
from fastapi.responses import HTMLResponse
from fastapi import Request

@app.get("/", response_class=HTMLResponse)
def show_page(request: Request):
    context = {
        "request": request, # 這是必要參數
        "my_variable": "Hello from Backend"
    }
    return templates.TemplateResponse("my_page.html", context)
```

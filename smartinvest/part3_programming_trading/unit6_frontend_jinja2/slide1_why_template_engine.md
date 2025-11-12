# 投影片 1/4: 為什麼需要模板引擎？

## 後端 (Backend) vs. 前端 (Frontend)

* **後端 (我們的 Python 程式)**:
  * 負責處理商業邏輯、資料庫存取、策略計算。
  * 產出的是「純資料」(e.g., JSON)。

* **前端 (使用者的瀏覽器)**:
  * 負責將資料「呈現」給使用者看。
  * 使用的是 HTML, CSS, JavaScript。

**問題**: 如何優雅地將後端產生的「資料」和前端的「HTML 結構」結合起來？

---

## 傳統的作法 (不推薦)

在 Python 程式中用字串拼接的方式硬幹出 HTML。

```python
html = "<h1>" + stock_name + "</h1>"
html += "<p>Price: " + str(stock_price) + "</p>"
return HTMLResponse(content=html)
```

* **缺點**: 混亂、難以維護、容易出錯、有安全性風險。

---

## 模板引擎 (Template Engine) 的作法

* **分離關注點 (Separation of Concerns)**。
* **Python (後端)**: 專心準備好資料 (一個字典)。
* **HTML 模板 (前端)**: 專心設計好頁面結構，並在需要的地方留下「佔位符」。
* **模板引擎**: 負責將資料填入佔位符，產生最終的 HTML。

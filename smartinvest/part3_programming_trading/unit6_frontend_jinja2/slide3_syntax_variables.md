# 投影片 3/4: Jinja2 基礎語法 (1) - 變數

## 在 HTML 中嵌入 Python 變數

---

## 分隔符 (Delimiters)

Jinja2 使用特定的分隔符來區分 HTML 標籤和模板語法：

* `{{ ... }}`: 用於 **印出變數** 或表達式的结果。
* `{% ... %}`: 用於 **流程控制**，例如 `for` 迴圈或 `if` 判斷。
* `{# ... #}`: 用於 **註解**，最終的 HTML 中不會顯示。

---

**變數渲染 `{{ ... }}`**

假設在 Python 中傳遞了這個 context:

```python
context = {
    "request": request,
    "stock": {"name": "台積電", "price": 600},
    "change_percent": 1.5
}
```

在 HTML 模板中可以這樣使用：

```html
<h1>{{ stock.name }}</h1>
<p>目前價格: {{ stock.price }}</p>
<p>漲跌幅: {{ change_percent }}%</p>
```

**渲染結果:**

```html
<h1>台積電</h1>
<p>目前價格: 600</p>
<p>漲跌幅: 1.5%</p>
```

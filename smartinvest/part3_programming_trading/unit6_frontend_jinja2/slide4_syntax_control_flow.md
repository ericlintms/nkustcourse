# 投影片 4/4: Jinja2 基礎語法 (2) - 流程控制

## 讓你的 HTML 模板動起來

---

**For 迴圈 `{% for ... %}`**

用於遍歷一個序列 (例如 Python 的 list)。

**Python:**

```python
context['stocks'] = [
    {"id": "2330", "name": "台積電"},
    {"id": "2454", "name": "聯發科"}
]
```

**HTML 模板:**

```html
<ul>
    {% for s in stocks %}
        <li>{{ s.id }} - {{ s.name }}</li>
    {% endfor %}
</ul>
```

**渲染結果:**

```html
<ul>
    <li>2330 - 台積電</li>
    <li>2454 - 聯發科</li>
</ul>
```

---

**If 判斷 `{% if ... %}`**

用於根據條件顯示不同的內容。

**HTML 模板:**

```html
<p class="{% if stock.change > 0 %}positive{% else %}negative{% endif %}">
    {{ stock.price }}
</p>
```

* 如果 `stock.change` > 0，class 會是 `positive`。
* 反之，class 會是 `negative`。

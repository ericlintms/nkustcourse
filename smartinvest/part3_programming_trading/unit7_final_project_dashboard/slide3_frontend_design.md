# 投影片 3/4: 前端設計 - HTML & Jinja2

## 我們需要一個 `dashboard.html` 模板，它要能處理兩種狀態

### 狀態 1: 初始狀態 (沒有回測結果)

* 當 `stats` 這個變數不存在時，顯示提示訊息，例如「請在左側輸入參數並執行回測」。

### 狀態 2: 顯示結果狀態

* 當 `stats` 變數存在時，才顯示結果區塊。

---

**使用 `{% if stats %}` 來控制**

```html
{% if stats %}
    <!-- 這裡是顯示結果的區塊 -->
    <table>
        <!-- 用 for 迴圈印出績效指標 -->
        {% for key, value in stats.items() %}
            <tr> ... </tr>
        {% endfor %}
    </table>
    <canvas id="equityChart"></canvas>
{% else %}
    <!-- 這裡是顯示提示訊息的區塊 -->
    <p>請執行回測...</p>
{% endif %}
```

---

## HTML 表單

* `<form>` 標籤的 `action` 屬性要對應到 FastAPI 的路徑 (`/run_backtest`)。
* `method` 屬性要設為 `post`。
* 每一個 `<input>` 都要有 `name` 屬性，這個 `name` 必須和 FastAPI 函式中接收的參數名稱一致。

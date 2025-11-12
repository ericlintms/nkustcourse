# 投影片 4/4: 前端圖表 - Chart.js

## Jinja2 負責產生 HTML，但它不能直接畫圖

我們需要在瀏覽器端，使用 JavaScript 的圖表函式庫來繪製動態圖表。

**Chart.js: 一個熱門、簡單易用的 JavaScript 圖表庫。**

---

## 整合流程

1. **後端 (Python)**:
    * 在執行完回測後，從 `stats` 物件中取得資金曲線的數據。
    * `stats['_equity_curve']['Equity']` 是一個 Pandas Series，包含了日期和對應的資金。
    * 將這個 Series 轉換為 **JSON 格式** 的字串，並傳遞給 Jinja2 模板。

    ```python
    context["equity_curve"] = stats['_equity_curve']['Equity'].to_json()
    ```

2. **前端 (HTML/JavaScript)**:
    * 在 HTML 的 `<head>` 中，用 CDN 的方式引入 Chart.js 的主程式。
    * 在 `<body>` 中，建立一個 `<canvas>` 元素作為圖表的畫布。
    * 在 `<script>` 標籤中：
        * 用 `{{ equity_curve | safe }}` 來接收後端傳來的 JSON 字串。
        ( `| safe` 是告訴 Jinja2 不要對這個字串進行 HTML 跳脫)。
        * 解析 JSON 資料，並用它來初始化 Chart.js。

# 單元 6: 前端互動介面 - Jinja2

API 回傳的 JSON 格式對程式很友好，但對人類不直觀。本單元將學習如何使用 Jinja2 模板引擎，將後端資料渲染成使用者看得懂的 HTML 網頁。

## 學習目標

- 了解什麼是模板引擎
- 學會在 FastAPI 中設定並使用 Jinja2
- 掌握 Jinja2 的基本語法，在 HTML 中嵌入動態資料

### 內容

1. **什麼是模板引擎？**
    - 將「資料」和「表現」分離的工具。
    - HTML 模板 + 資料 -> 最終的 HTML 網頁。
2. **在 FastAPI 中整合 Jinja2**
    - 安裝: `pip install jinja2`
    - 設定 `Jinja2Templates`。
    - 在路徑操作函式中回傳 `TemplateResponse`。
3. **Jinja2 語法**
    - 變數渲染: `{{ variable }}`
    - 流程控制: `{% for item in items %}` 和 `{% if condition %}`

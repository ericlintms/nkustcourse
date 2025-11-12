# 投影片 2/4: 後端設計 - FastAPI

## 我們需要兩個 API 端點 (Endpoints)

---

**1. `GET /`**

* **目的**: 提供儀表板的「初始頁面」。
* **HTTP 方法**: `GET` (因為只是單純地取得頁面)。
* **實作**:
  * 定義一個 `get_dashboard()` 函式。
  * 使用 `@app.get("/")` 裝飾器。
  * 函式內部很簡單，只需要回傳一個 `TemplateResponse`，渲染一個不帶任何回測結果的 `dashboard.html` 即可。

---

**2. `POST /run_backtest`**

* **目的**: 接收參數、執行回測、並回傳包含結果的頁面。
* **HTTP 方法**: `POST` (因為使用者正在「提交」資料來觸發一個動作)。
* **實作**:
  * 定義一個 `run_backtest()` 函式。
  * 使用 `@app.post("/run_backtest")` 裝飾器。
  * 使用 `Form(...)` 來接收來自 HTML 表單的參數。
  * 呼叫 `Backtest(...).run()`。
  * 將 `stats` 結果打包到 context 字典中。
  * 回傳 `TemplateResponse`，渲染同一個 `dashboard.html`，但這次帶上了回測結果。

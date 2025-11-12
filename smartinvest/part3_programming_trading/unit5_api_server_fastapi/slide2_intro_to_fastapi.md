# 投影片 2/4: 認識 FastAPI

## 一個現代、高效能的 Python Web 框架

框架 (Framework) 就像是蓋房子的鷹架，它幫你搭好了基本的結構，你只需要專注在填上自己的內容 (業務邏輯)。

---

## 為什麼選擇 FastAPI？

1. **Fast (快速)**: 如其名，它是目前 Python Web 框架中效能的佼佼者之一，
與 Node.js, Go 並駕齊驅。

2. **Easy to Code (易於撰寫)**: 語法非常簡潔直觀，開發速度快。

3. **Automatic Docs (自動文件)**: **殺手級功能！** FastAPI 會自動根據你的程式碼，
產生兩種互動式的 API 文件 (Swagger UI 和 ReDoc)。你再也不用手寫 API 文件了！

4. **Type Hints (型別提示)**: 大量使用 Python 的型別提示，這讓你的程式碼更穩健，編輯器也能提供更好的自動補全和錯誤檢查。

---

## 安裝

我們需要安裝兩個東西：

1. `fastapi`: 框架本身。
2. `uvicorn`: 一個高效能的 ASGI 伺服器，用來「運行」我們的 FastAPI 應用。

```bash
pip install fastapi "uvicorn[standard]"
```

# 範例 1: FastAPI Hello World

# 檔名: main.py
# 執行: 在終端機輸入 uvicorn main:app --reload

from fastapi import FastAPI

# 1. 建立一個 FastAPI 實例
app = FastAPI()

# 2. 定義一個「路徑操作」 (Path Operation)
# @app.get("/") 是一個「裝飾器」
# 它告訴 FastAPI，當有瀏覽器或程式對 "/" 這個路徑發出 GET 請求時，
# 就執行下面的函式。
@app.get("/")
def read_root():
    # 3. 函式回傳的內容，會被自動轉換為 JSON 格式並發送給客戶端
    return {"message": "Hello, FastAPI!"}

@app.get("/ping")
def ping():
    return {"response": "pong"}

# --- 如何測試 ---
# 1. 儲存檔案為 main.py
# 2. 在終端機中，切換到這個檔案所在的目錄
# 3. 執行指令: uvicorn main:app --reload
# 4. 打開瀏覽器，輸入 http://127.0.0.1:8000/，你會看到 {"message":"Hello, FastAPI!"}
# 5. 接著試試 http://127.0.0.1:8000/ping
# 6. 厲害的來了，打開 http://127.0.0.1:8000/docs，你會看到 FastAPI 自動產生的互動式 API 文件！

from fastapi import FastAPI

# 建立一個 FastAPI 應用實例
app = FastAPI()

# 使用 @app.get("/path") 裝飾器來定義一個 GET 請求的端點
@app.get("/hello")
def read_hello():
    """
    這個端點會回傳一個固定的 JSON 問候訊息。
    """
    return {"message": "Hello, Trader!"}

# --- 如何執行這個伺服器 ---
# 1. 將此程式碼儲存為一個 .py 檔案 (例如: main.py)。
# 2. 在你的終端機 (terminal) 中，切換到該檔案所在的目錄。
# 3. 執行以下指令:
#    uvicorn main:app --reload
#    (main 是檔名, app 是 FastAPI 的實例名稱)
# 4. 打開你的瀏覽器，然後前往 http://127.0.0.1:8000/hello

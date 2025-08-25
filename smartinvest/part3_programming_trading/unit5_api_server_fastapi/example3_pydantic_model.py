# 範例 3: 使用 Pydantic 模型接收資料

# 檔名: main.py
# 當你要接收的資料結構比較複雜時，使用 Pydantic 模型是更專業、更穩健的做法。

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# --- 1. 定義你的資料模型 ---
# 建立一個 Class，繼承自 pydantic 的 BaseModel
# FastAPI 會自動用它來做資料驗證、轉換，並產生在 API 文件中
class Stock(BaseModel):
    id: str
    name: str
    price: float
    tags: List[str] = [] # tags 是一個字串的列表，預設為空列表

app = FastAPI()

# --- 2. 在路徑操作函式中使用模型 ---
# 使用 POST 方法來接收資料
# 函式參數的型別註記為我們定義的 Stock 模型
@app.post("/stocks/")
def create_stock(stock: Stock):
    # FastAPI 會自動將請求的 body (必須是 JSON 格式) 解析並驗證為一個 Stock 物件
    print(f"接收到股票資料: {stock.name}")
    
    # 你可以直接操作這個物件
    if stock.price > 1000:
        print(f"{stock.name} 是高價股！")

    return {"message": f"Stock {stock.name} created successfully.", "data": stock}

# --- 如何測試 ---
# 1. 執行 uvicorn main:app --reload
# 2. 打開 http://127.0.0.1:8000/docs
# 3. 找到 /stocks/ 的 POST 端點，點開它
# 4. 點擊 "Try it out"
# 5. 在 Request body 中，輸入 JSON 格式的資料，例如：
#    {
#      "id": "3008",
#      "name": "大立光",
#      "price": 2500,
#      "tags": ["Apple", "Camera"]
#    }
# 6. 點擊 "Execute"，看看伺服器端的回應和終端機的輸出。
# 7. 試著輸入錯誤的資料型態 (e.g., price 給一個字串)，看看 FastAPI 自動產生的錯誤訊息。

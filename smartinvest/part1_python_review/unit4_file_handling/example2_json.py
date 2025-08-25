# 範例 2: 讀寫 JSON 檔案

import json

# --- 寫入 JSON ---
data_to_write = {
    "stock_id": "2330",
    "stock_name": "台積電",
    "market": "TSE",
    "is_active": True,
    "history_prices": [
        {"date": "2023-10-01", "price": 600},
        {"date": "2023-10-02", "price": 605}
    ]
}

file_path = 'stock_info.json'

with open(file_path, 'w', encoding='utf-8') as jsonfile:
    # indent=4 讓 JSON 格式更容易閱讀
    json.dump(data_to_write, jsonfile, ensure_ascii=False, indent=4)

print(f"資料已寫入 {file_path}")

# --- 讀取 JSON ---
with open(file_path, 'r', encoding='utf-8') as jsonfile:
    data_read = json.load(jsonfile)
    print(f"\n從 {file_path} 讀取資料:")
    print(data_read)
    print(f"股票名稱: {data_read['stock_name']}")
    print(f"第一天的歷史價格: {data_read['history_prices'][0]}")


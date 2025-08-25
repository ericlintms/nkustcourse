# 範例 1: 讀寫 CSV 檔案

import csv

# --- 寫入 CSV ---
data_to_write = [
    ['Date', 'Open', 'High', 'Low', 'Close'],
    ['2023-10-01', 120, 122, 119, 121],
    ['2023-10-02', 121, 123, 120, 122]
]

file_path = 'stock_prices.csv'

with open(file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data_to_write)

print(f"資料已寫入 {file_path}")

# --- 讀取 CSV ---
with open(file_path, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader) # 讀取標頭
    print(f"\n從 {file_path} 讀取資料:")
    print(f"標頭: {header}")
    for row in reader:
        print(row)

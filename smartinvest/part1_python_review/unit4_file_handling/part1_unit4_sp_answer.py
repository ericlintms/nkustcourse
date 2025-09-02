import csv
import os

# --- Part 1: 建立 CSV 檔案 ---
file_path = 'products.csv'
header = ['product_id', 'product_name', 'price']
data = [
    {'product_id': '1', 'product_name': 'Laptop', 'price': '1200'},
    {'product_id': '2', 'product_name': 'Mouse', 'price': '25'},
    {'product_id': '3', 'product_name': 'Keyboard', 'price': '75'}
]

try:
    # 在當前工作目錄下建立檔案
    full_path = os.path.join(os.getcwd(), file_path)

    with open(full_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        writer.writerows(data)
    print(f'\' {full_path}\' created successfully.')

    # --- Part 2: 讀取 CSV 檔案 ---
    print(f'\nReading from \' {full_path}\'')
    with open(full_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(dict(row))

except IOError as e:
    print(f'An I/O error occurred: {e}')

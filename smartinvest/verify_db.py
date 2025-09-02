import sqlite3

conn = sqlite3.connect('twse_data.db')
cursor = conn.cursor()

# 檢查股票資料筆數
cursor.execute('SELECT COUNT(*) FROM stocks')
stock_count = cursor.fetchone()[0]
print(f'股票資料筆數: {stock_count}')

# 檢查指數資料筆數
cursor.execute('SELECT COUNT(*) FROM indices')
index_count = cursor.fetchone()[0]
print(f'指數資料筆數: {index_count}')

# 顯示前3支股票
cursor.execute('SELECT code, name, close FROM stocks LIMIT 3')
print('前3支股票:')
for row in cursor.fetchall():
    print(row)

# 顯示前3個指數
cursor.execute('SELECT name, close, change_percent FROM indices LIMIT 3')
print('前3個指數:')
for row in cursor.fetchall():
    print(row)

conn.close()

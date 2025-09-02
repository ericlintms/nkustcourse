import sqlite3

conn = sqlite3.connect('twse_data.db')
cursor = conn.cursor()

# 檢查股票資料的漲跌欄位
cursor.execute('SELECT code, name, close, color, symbol FROM stocks LIMIT 5')
print('前5支股票的漲跌資訊:')
for row in cursor.fetchall():
    print(row)

# 檢查不同漲跌類型的統計
cursor.execute('SELECT color, symbol, COUNT(*) FROM stocks GROUP BY color, symbol')
print('\n漲跌統計:')
for row in cursor.fetchall():
    print(f'{row[0]} {row[1]}: {row[2]} 支股票')

conn.close()

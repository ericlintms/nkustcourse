import matplotlib.pyplot as plt

# 數據
years = [2018, 2019, 2020, 2021, 2022]
sales = [10, 12, 15, 14, 18]

# 建立一個新的圖表
plt.figure(figsize=(8, 5))

# 繪製折線圖，並在資料點上加上標記
plt.plot(years, sales, marker='o')

# 加上標題和軸標籤
plt.title('Annual Sales')
plt.xlabel('Year')
plt.ylabel('Sales (in millions)')

# 加上格線方便閱讀
plt.grid(True)

# 顯示圖表
plt.show()

# 要執行此腳本，請先安裝 matplotlib:
# pip install matplotlib

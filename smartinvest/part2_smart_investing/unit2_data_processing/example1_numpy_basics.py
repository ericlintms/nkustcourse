# 範例 1: NumPy 基礎

import numpy as np

# 從 Python list 建立 NumPy array
prices_list = [120.5, 121.0, 120.0, 122.5, 125.0]
prices_array = np.array(prices_list)

print(f"Python list: {prices_list}")
print(f"NumPy array: {prices_array}")

# NumPy array 的主要優點：可以對整個陣列進行數學運算
# 假設我們要將所有價格都加上 5 元

# Python list 的作法 (需要用迴圈)
prices_list_plus_5 = [p + 5 for p in prices_list]
print(f"List 加 5: {prices_list_plus_5}")

# NumPy array 的作法 (直接運算，更簡潔、更快速)
prices_array_plus_5 = prices_array + 5
print(f"Array 加 5: {prices_array_plus_5}")

# 計算平均值和標準差
mean = np.mean(prices_array)
std_dev = np.std(prices_array)

print(f"平均價格: {mean:.2f}")
print(f"價格標準差: {std_dev:.2f}")

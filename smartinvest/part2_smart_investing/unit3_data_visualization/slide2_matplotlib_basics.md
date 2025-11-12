# 投影片 2/4: Matplotlib 繪圖基礎

## Matplotlib: Python 可視化的瑞士刀

* 它是 Python 最老牌、最基礎，也是最多人使用的繪圖函式庫。
* Pandas 的內建繪圖功能，底層也是呼叫 Matplotlib。

---

## 繪圖的基本步驟 (The pyplot API)

`pyplot` 是 Matplotlib 中最常用的模組，提供了一個類似 MATLAB 的繪圖介面。

```python
import matplotlib.pyplot as plt

# 1. 準備資料 (通常是 list 或 pandas Series)
x_data = [1, 2, 3, 4]
y_data = [10, 20, 15, 25]

# 2. 建立圖表 (figure) 和座標軸 (axes)
plt.figure(figsize=(8, 4)) # figsize 是圖的大小

# 3. 繪製圖表
plt.plot(x_data, y_data) # .plot() 是折線圖

# 4. (可選) 客製化圖表
plt.title("My First Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# 5. 顯示圖表
plt.show()
```
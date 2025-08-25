# 範例 3: 函式與模組

# 引用 Python 內建的 math 模組
import math

# 自訂函式 - 計算報酬率
def calculate_return(start_price, end_price):
    """計算給定開始與結束價格的報酬率"""
    return (end_price - start_price) / start_price * 100

# 使用函式
roi = calculate_return(100, 120)
print(f"報酬率: {roi:.2f}%")

# 使用 math 模組中的函式
print(f"144 的平方根是: {math.sqrt(144)}")

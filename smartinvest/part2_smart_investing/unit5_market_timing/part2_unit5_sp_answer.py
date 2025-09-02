def simple_moving_average(prices, window):
    """
    計算給定價格列表的簡單移動平均線 (SMA)。
    這個版本為了易於理解，可讀性較高。
    """
    # 如果資料長度小於窗口大小，無法計算
    if window > len(prices):
        return []
    
    averages = []
    # 從第一個窗口開始，滑動到最後
    for i in range(len(prices) - window + 1):
        # 取出當前窗口的數據
        window_slice = prices[i:i+window]
        # 計算平均值並加入列表
        averages.append(sum(window_slice) / window)
        
    return averages

# 範例
price_data = [10, 12, 11, 13, 15, 14, 16, 18, 17, 20]
window_size = 3
sma = simple_moving_average(price_data, window_size)

print(f"原始價格: {price_data}")
# SMA 列表的長度會比原始資料短 (window_size - 1)
print(f"{window_size} 日簡單移動平均線: {[f'{avg:.2f}' for avg in sma]}")

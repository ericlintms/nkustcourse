def calculate_portfolio_return(weights, returns):
    """
    計算投資組合的預期回報率。
    """
    # 檢查兩個列表的長度是否一致
    if len(weights) != len(returns):
        return "Error: Weights and returns lists must have the same number of elements."

    # 檢查權重總和是否約等於 1 (使用容忍度來處理浮點數誤差)
    if not (0.999 < sum(weights) < 1.001):
        return f"Error: Weights must sum to 1. Current sum is {sum(weights)}."

    total_return = 0
    # 使用 zip 同時遍歷權重和回報率
    for weight, expected_return in zip(weights, returns):
        total_return += weight * expected_return

    return total_return

# 範例 1: 正常情況
asset_weights = [0.5, 0.3, 0.2]  # 50% 股票, 30% 債券, 20% 黃金
expected_returns = [0.10, 0.05, 0.15] # 各資產的預期回報率

portfolio_return = calculate_portfolio_return(asset_weights, expected_returns)

# 檢查回傳的是否為數字，以判斷計算是否成功
if isinstance(portfolio_return, (int, float)):
    print(f"投資組合的預期回報率為: {portfolio_return:.2%}")

print("-"*20)

# 範例 2: 權重總和不為 1
bad_weights = [0.5, 0.3, 0.3]
error_message = calculate_portfolio_return(bad_weights, expected_returns)
print(f"使用錯誤的權重: {error_message}")

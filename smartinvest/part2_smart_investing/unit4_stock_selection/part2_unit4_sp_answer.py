def calculate_pe_ratio(price_per_share, earnings_per_share):
    """
    計算本益比 (P/E Ratio)。
    如果每股盈餘為 0 或負數，則回傳 None。
    """
    if not isinstance(price_per_share, (int, float)) or not isinstance(earnings_per_share, (int, float)):
        return "Invalid input, please provide numbers."

    if earnings_per_share <= 0:
        return None
    
    return price_per_share / earnings_per_share

# 範例 1: 正常情況
price = 150
eps = 7.5
pe_ratio = calculate_pe_ratio(price, eps)
print(f"情況 1: Price=${price}, EPS=${eps}")
print(f"本益比為: {pe_ratio:.2f}")

print("-"*20)

# 範例 2: EPS 為 0
price = 100
eps_zero = 0
pe_ratio_zero = calculate_pe_ratio(price, eps_zero)
print(f"情況 2: Price=${price}, EPS=${eps_zero}")
print(f"本益比為: {pe_ratio_zero}")

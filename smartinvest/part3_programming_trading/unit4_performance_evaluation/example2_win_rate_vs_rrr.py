# 範例 2: 勝率 vs 賺賠比

import pandas as pd

# 假設有兩個策略的回測交易紀錄
strategy_A_trades = pd.Series([5, 5, 5, 5, -10, -10]) # 高勝率，但一次賠大的
strategy_B_trades = pd.Series([20, -5, -5, -5, -5]) # 低勝率，但一次賺大的

def analyze_trades(trades, strategy_name):
    print(f"--- 分析策略 {strategy_name} ---")
    
    # 總損益
    total_profit = trades.sum()
    print(f"總損益: {total_profit}")

    # 勝率
    win_rate = (trades > 0).mean() * 100
    print(f"勝率: {win_rate:.2f}%")

    # 平均獲利
    avg_win = trades[trades > 0].mean()
    print(f"平均獲利: {avg_win:.2f}")

    # 平均虧損
    avg_loss = abs(trades[trades < 0].mean())
    print(f"平均虧損: {avg_loss:.2f}")

    # 賺賠比 (Reward-to-Risk Ratio)
    if avg_loss > 0:
        reward_risk_ratio = avg_win / avg_loss
        print(f"賺賠比: {reward_risk_ratio:.2f}")
    else:
        print("賺賠比: N/A (沒有虧損交易)")
    
    print("\n")

analyze_trades(strategy_A_trades, "A (高勝率)")
analyze_trades(strategy_B_trades, "B (低勝率)")

# --- 結論 ---
# 策略 A 的勝率高達 66.67%，但賺賠比只有 0.5 (賺的時候賺5元，賠的時候賠10元)，導致總損益為 0。
# 策略 B 的勝率只有 20%，但賺賠比高達 4.0 (賺的時候賺20元，賠的時候賠5元)，最終總損益為 0。
# 在這個例子中，兩個策略最終都沒賺錢，但它揭示了：
# **只看勝率是危險的，必須同時考慮賺賠比，才能評估策略的真實期望值。**

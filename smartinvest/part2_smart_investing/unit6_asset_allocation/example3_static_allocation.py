# 範例 3: 簡單的靜態資產配置模型

import pandas as pd
import matplotlib.pyplot as plt

# 假設有兩支ETF的歷史價格
data = {
    'SPY': [100, 102, 101, 105, 103], # 追蹤美國股市的ETF
    'AGG': [50, 50.1, 49.9, 49.8, 50.2]  # 追蹤美國債市的ETF
}
df = pd.DataFrame(data)

class StaticPortfolio:
    def __init__(self, initial_capital, weights):
        self.capital = initial_capital
        self.weights = weights
        self.portfolio_value = pd.Series()

    def run_simulation(self, prices_df):
        returns = prices_df.pct_change().dropna()
        
        # 計算每日的投資組合報酬
        # .dot() 是矩陣乘法，可以快速計算加權總和
        portfolio_returns = returns.dot(pd.Series(self.weights))
        
        # 計算每日的投資組合價值
        # (1 + portfolio_returns).cumprod() 計算累積報酬
        self.portfolio_value = self.capital * (1 + portfolio_returns).cumprod()
        # 將第一天的起始資金補上
        self.portfolio_value.iloc[0] = self.capital

    def plot_performance(self):
        if not self.portfolio_value.empty:
            self.portfolio_value.plot(figsize=(10, 6),
                                      title='Portfolio Performance')
            plt.ylabel('Portfolio Value')
            plt.grid(True)
            plt.show()
        else:
            print("Please run the simulation first.")

# --- 執行模擬 ---
# 初始資金 10000 元
# 股債比 70/30
portfolio = StaticPortfolio(initial_capital=10000, 
                            weights={'SPY': 0.7, 'AGG': 0.3})

portfolio.run_simulation(df)

print("--- 投資組合每日價值 ---")
print(portfolio.portfolio_value)

portfolio.plot_performance() # 需要 matplotlib

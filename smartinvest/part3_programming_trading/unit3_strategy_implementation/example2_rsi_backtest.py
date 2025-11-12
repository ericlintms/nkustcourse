# 範例 2: 回測 RSI 超買超賣策略

from backtesting import Backtest, Strategy
from backtesting.test import RSI, GOOG

class RsiOscillator(Strategy):
    # 策略參數
    rsi_period = 14
    oversold_threshold = 30
    overbought_threshold = 70

    def init(self):
        # 計算 RSI 指標
        self.rsi = self.I(RSI, self.data.Close, self.rsi_period)

    def next(self):
        # 如果 RSI 跌破超賣區，買入
        if self.rsi[-1] < self.oversold_threshold:
            if not self.position:
                self.buy()
        
        # 如果 RSI 突破超買區，賣出
        elif self.rsi[-1] > self.overbought_threshold:
            if self.position:
                self.sell()

# --- 執行回測 ---
bt = Backtest(GOOG, RsiOscillator, cash=10000, commission=.002)
stats = bt.run()

print("--- RSI 超買超賣策略回測結果 ---")
print(stats)
bt.plot()

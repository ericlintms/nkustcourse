from backtesting import Strategy

# backtesting.py 需要特定格式的數據 (Open, High, Low, Close, Volume)
# 在這個範例中，我們只是定義類別，所以不需要真實數據。

class MyFirstStrategy(Strategy):
    def init(self):
        # init 方法在回測開始時執行一次，用於初始化設定或預先計算指標。
        pass

    def next(self):
        # next 方法在每個數據點（例如，每一天）都會被呼叫。
        # 這裡是放置主要交易邏輯的地方。
        pass

# --- 補充：如何執行 --- 
# 僅僅定義類別是練習的目標。若要實際執行回測，你需要：
# 1. 準備符合格式的市場數據 (例如從 backtesting.test 導入 GOOG)。
# 2. 建立 Backtest 物件並執行 .run()。
#
# from backtesting import Backtest
# from backtesting.test import GOOG
# bt = Backtest(GOOG, MyFirstStrategy, commission=.002)
# stats = bt.run()
# print(stats)

print("策略類別 'MyFirstStrategy' 已成功定義。")
print("這是使用 backtesting.py 函式庫建立策略的基本結構。")

# 要執行此腳本，請先安裝 backtesting.py:
# pip install backtesting

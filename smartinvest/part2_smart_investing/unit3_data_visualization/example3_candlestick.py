# 範例 3: 繪製 K 線圖 (Candlestick Chart)

# 需要先安裝 mplfinance: pip install mplfinance
import pandas as pd
import mplfinance as mpf

# 準備具有 Open, High, Low, Close, Volume 的資料
# 這些是繪製 K 線圖的標準欄位名稱 (大小寫要一樣)
data = {
    'Open': [600, 606, 610, 603, 608],
    'High': [605, 610, 612, 608, 615],
    'Low': [598, 605, 602, 601, 607],
    'Close': [605, 610, 603, 608, 614],
    'Volume': [50000, 55000, 48000, 60000, 52000]
}
index = pd.to_datetime(['2023-10-01', '2023-10-02', '2023-10-03', '2023-10-04', '2023-10-05'])
df = pd.DataFrame(data, index=index)

# --- 使用 mplfinance 繪圖 ---
# mpf.plot() 會自動處理大部分的設定
mpf.plot(df, 
         type='candle', # 指定圖表類型為 K 線圖
         title='Stock Candlestick Chart', 
         ylabel='Price ($)',
         volume=True, # 在下方加入成交量圖
         ylabel_lower='Volume',
         style='yahoo', # 設定樣式
         figsize=(12, 7)
        )

# --- 加入移動平均線 ---
mpf.plot(df, 
         type='candle', 
         title='Candlestick Chart with Moving Averages', 
         ylabel='Price ($)',
         volume=True, 
         ylabel_lower='Volume',
         style='yahoo', 
         figsize=(12, 7),
         mav=(3, 5) # 加入 3 日和 5 日移動平均線
        )

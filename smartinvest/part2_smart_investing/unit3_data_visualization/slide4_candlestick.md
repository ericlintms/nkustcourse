# 投影片 4/4: 金融圖表之王 - K線圖

## 為什麼需要 K 線圖 (Candlestick Chart)？

一張小小的 K 棒，包含了四個關鍵價格資訊：

* **開盤價 (Open)**
* **最高價 (High)**
* **最低價 (Low)**
* **收盤價 (Close)**

它比單純的收盤價折線圖提供了更豐富的市場情緒資訊。

![Candlestick](https://www.investopedia.com/thmb/d32_ML_a_g3-2-83v-32-Y_g=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/CandlestickChart-1024x768-269ba5809759407898a1d63f6a3d7443.png)

---

## 使用 `mplfinance` 簡化繪圖

雖然 Matplotlib 也能畫 K 線，但過程繁瑣。`mplfinance` 是專為金融圖表設計的套件，能讓我們用一行程式碼就畫出專業的 K 線圖。

### 資料準備是關鍵

DataFrame 的欄位名稱必須是 `Open`, `High`, `Low`, `Close`, `Volume` (首字大寫)。

```python
import mplfinance as mpf

# df 是一個準備好的 DataFrame
mpf.plot(df,
         type='candle',       # 圖表類型
         volume=True,         # 顯示成交量
         mav=(5, 20),         # 加上 5日 和 20日 移動平均線
         style='charles'      # 內建樣式
        )
```
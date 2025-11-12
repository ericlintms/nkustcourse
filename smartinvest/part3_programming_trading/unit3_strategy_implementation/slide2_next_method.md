# 投影片 2/4: 關鍵的 `next()` 方法

`next()` 是策略的心臟，它會在每個時間點被呼叫，用來做交易決策。

---

## 存取資料和指標

* `self.data`: 存取 OHLCV 資料。
  * `self.data.Close`: 存取收盤價序列。
  * `self.data.Close[-1]`: 存取「前一根」K棒的收盤價 (最新已收盤的價格)。
  * `self.data.Close[0]`: 存取「當前」K棒的收盤價 (在 `next` 中通常代表最新價)。
* `self.ma[-1]`: 存取指標的「前一期」數值。

## 管理部位 (Position)

* `self.position`: 代表你目前的持倉狀態。
  * `if self.position:`: 判斷目前是否持倉。
  * `if not self.position:`: 判斷目前是否空手。
  * `self.position.is_long`: 是否持有多頭部位。
  * `self.position.is_short`: 是否持有空頭部位。

## 下單指令

* `self.buy()`: 買入 (預設買滿)。
* `self.sell()`: 賣出 (預設賣光)。
* `self.position.close()`: 平倉。

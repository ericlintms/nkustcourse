# 投影片 2/4: 類別 (Class) 與 物件 (Object)

## 類別 (Class): 物件的藍圖

* Class 是一個模板，用來定義物件應該有哪些 **屬性 (attributes)** 和 **方法 (methods)**。
* 就像是「汽車設計圖」。

## 物件 (Object): 藍圖的實例

* Object 是根據 Class 這個藍圖實際建立出來的東西。
* 就像是根據「汽車設計圖」生產出來的「一輛車」。

---

## 從藍圖到實體

```python
# Class: 定義了「股票」這個概念
class Stock:
    # 建構函式: 初始化物件的屬性
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # Method: 定義了物件可以做什麼事
    def display(self):
        print(f"{self.name} 的價格是 {self.price}")

# Object: 建立兩個實際的股票物件
tsmc = Stock("台積電", 600)
mediatek = Stock("聯發科", 900)

# 每一輛車 (物件) 都是獨立的
tsmc.display()
mediatek.display()
```

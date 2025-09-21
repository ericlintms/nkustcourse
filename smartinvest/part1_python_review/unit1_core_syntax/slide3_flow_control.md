# 投影片 3/4: 流程控制

讓程式可以根據不同的情況，做出不同的反應。

---

## **條件判斷 (if/elif/else)**

```python
if price > 600:
    print("價格偏高，考慮賣出")
elif price < 580:
    print("價格偏低，考慮買入")
else:
    print("價格穩定，持續觀察")
```

---

## **迴圈 (for / while)**

* `for`: 用於遍歷一個序列 (例如 List)
* `while`: 用於當某個條件為真時，重複執行

```python
# For 迴圈
for p in prices:
    print(f"今日價格: {p}")

# While 迴圈
count = 0
while count < 3:
    print("執行第", count, "次檢查")
    count += 1
```

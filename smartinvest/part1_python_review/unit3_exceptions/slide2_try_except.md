# 投影片 2/4: 使用 `try...except` 捕捉例外

## 基本語法

將你 **預期可能出錯** 的程式碼，放在 `try` 區塊中。

如果真的發生錯誤，Python 會產生一個「例外物件」，並跳到對應的 `except` 區塊去執行。

```python
try:
    # --- 試著做這些事 ---
    age = int(input("請輸入你的年齡: "))
    risk = 10 / age
    print(f"你的風險指數是 {risk}")

except ValueError:
    # --- 如果發生 ValueError (例如輸入非數字) --- #
    print("輸入無效，請確定你輸入的是數字。")

except ZeroDivisionError:
    # --- 如果發生 ZeroDivisionError (例如輸入 0) --- #
    print("年齡不能為 0，無法計算風險。")

print("程式繼續執行...")
```

## 重點

程式不會崩潰，而是會執行 `except` 裡的程式碼，然後繼續往下走。

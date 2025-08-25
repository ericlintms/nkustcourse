# 範例 1: 基本例外處理

def divide(x, y):
    try:
        result = x / y
        print(f"結果是: {result}")
    except ZeroDivisionError:
        print("錯誤: 除數不能為零！")
    except TypeError:
        print("錯誤: 輸入的型態不正確，請確認皆為數字")
    finally:
        print("--- 運算結束 ---")

# 正常情況
divide(10, 2)

# 發生 ZeroDivisionError
divide(10, 0)

# 發生 TypeError
divide("a", 2)

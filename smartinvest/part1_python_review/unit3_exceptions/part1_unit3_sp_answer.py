def divide_numbers(a, b):
    """
    將 a 除以 b，並處理 ZeroDivisionError 和 TypeError。
    """
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except TypeError:
        return "Error: Both inputs must be numbers."
    else:
        return result

# 範例
print(f"10 / 2 = {divide_numbers(10, 2)}")
print(f"10 / 0 = {divide_numbers(10, 0)}")
print(f"10 / 'a' = {divide_numbers(10, 'a')}")

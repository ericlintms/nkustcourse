# 範例 2: 引發例外 (raise)

def set_age(age):
    if not isinstance(age, int):
        raise TypeError("年齡必須是整數")
    if age < 0 or age > 120:
        raise ValueError("年齡必須在 0 到 120 之間")
    print(f"年齡已設定為: {age}")

try:
    set_age(25)
    set_age(-10) # 這行會引發 ValueError
except ValueError as e:
    print(f"設定失敗: {e}")

try:
    set_age("secret") # 這行會引發 TypeError
except TypeError as e:
    print(f"設定失敗: {e}")

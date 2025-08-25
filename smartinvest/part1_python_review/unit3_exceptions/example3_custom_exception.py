# 範例 3: 自訂例外

# 自訂一個用於交易的例外類別
class TradingError(Exception):
    """與交易相關操作的基礎例外"""
    pass

class InsufficientFundsError(TradingError):
    """當帳戶資金不足時引發的例外"""
    def __init__(self, current_balance, required_amount):
        self.current_balance = current_balance
        self.required_amount = required_amount
        message = f"資金不足。目前餘額: {current_balance}, 需要: {required_amount}"
        super().__init__(message)

# 模擬一個交易帳戶
class TradingAccount:
    def __init__(self, balance):
        self.balance = balance

    def buy_stock(self, price, quantity):
        total_cost = price * quantity
        if total_cost > self.balance:
            raise InsufficientFundsError(self.balance, total_cost)
        
        self.balance -= total_cost
        print(f"成功購買股票，花費: {total_cost}，剩餘資金: {self.balance}")


account = TradingAccount(10000)

try:
    account.buy_stock(50, 100) # 成功
    account.buy_stock(100, 80) # 失敗，資金不足
except InsufficientFundsError as e:
    print(f"交易失敗: {e}")

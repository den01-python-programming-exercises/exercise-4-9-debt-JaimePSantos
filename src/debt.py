class Debt:
  balance = 0.0
  interestRate = 0.0

  def __init__(self,initBalance,initIntRate):
    self.balance = initBalance
    self.interestRate = initIntRate
  
  def print_balance(self):
    print(self.balance)
  
  def wait_one_year(self):
    self.balance = self.balance * self.interestRate
    
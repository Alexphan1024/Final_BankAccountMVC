from account import Account
from .fees import fees
class Savings(Account):
    def __init__(self, name:str, balance:float = 0.0)->'None':
        super(Savings, self).__init__(name,balance)
        return

    def below_1000(self):
        if self.balance < 1000:
            self.balance = fees(self.balance).below_1000()
        if self.balance >= 1000:
            self.balance = fees(self.balance).interest()
        return

if __name__ == "__main__":
    sav_1= Savings("Hi",999)
    sav_1.deposit(700)
    print(sav_1.transaction())



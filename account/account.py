# account.py
#
# Alex Phan A01019714
from time import localtime, strftime
from .log_entry import Log
log = Log()

class Account:
    _NEXT_ACCT_NUM = 1000000000000000
    def __init__(self,name:str, balance:float = 0.0) -> "None":
        self.acct_num = Account._NEXT_ACCT_NUM
        self.name = name
        self.balance = balance
        Account._NEXT_ACCT_NUM += 1

    def withdraw(self,withdraw:float) -> float:
        self.balance = self.balance - withdraw
        log.adds(self.acct_num,strftime("%Y-%m-%d %H:%M:%S", localtime())," Withdraw $", withdraw)
        return self.balance

    def deposit(self, deposit:float)-> float:
        self.balance = self.balance + deposit
        log.adds(self.acct_num,strftime("%Y-%m-%d %H:%M:%S", localtime())," Deposit $", deposit)
        return self.balance

    @property
    def get_balance(self)-> float:
        return self.balance

    def set_balance(self,value:float)-> 'None':
        self.balance = value

    def change_name(self, new_name:str)-> str:
        self.name = new_name
        return self.name

    def transaction(self)->str:
        return log.shows_transaction(self.acct_num)


    def __str__(self)->str:
        return '{} \nName: {} \nAccount Number: {} \nAccount Balance: {} '.format(strftime("%Y-%m-%d %H:%M:%S", localtime()),self.name, self.acct_num, self.balance)

# if __name__ == "__main__":
#     act_1 = Account("Alex", 1000)
#     act_1.withdraw(500)
#     act_1.deposit(1000)
#     act_1.withdraw(500)
#     act_1.deposit(1000)
#     print(act_1)
#     print(act_1.transaction() + "\n")
#     print(act_1.balance)
#
#     act_2 = Account("Steve", 1000)
#     act_2.withdraw(5000)
#     act_2.deposit(10000)
#     act_2.withdraw(5000)
#     act_2.deposit(10000)
#     print(act_2)
#     print(act_2.transaction() + "\n")
#     pass
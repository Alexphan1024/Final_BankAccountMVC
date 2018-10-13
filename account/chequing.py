from account import Account
from .fees import fees
from time import localtime, strftime
from .log_entry import Log
log = Log()
class Chequing(Account):
    def __init__(self, name:str, balance:float = 0.0)->'None':
        super(Chequing, self).__init__(name,balance)
        self.bc = 25
        return

    def overdraft(self,withdraw:float)->float:
        if withdraw > self.balance:
            if withdraw > 500:
                print("Overdraft Max $500")
            else:
                self.balance = fees(self.balance).over_draft(withdraw)
                return self.balance
        else:
            self.balance = self.balance - withdraw
            log.adds(self.acct_num, strftime("%Y-%m-%d %H:%M:%S", localtime()), " Withdraw $", withdraw)
            return self.balance


    def bounce_cheque(self)->float:
        self.balance = fees(self.balance).bounced_cheque()
        log.adds(self.acct_num, strftime("%Y-%m-%d %H:%M:%S", localtime()), " Bounce Fee:", self.bc)
        return self.balance

if __name__ == "__main__":
    chq_1 = Chequing('Alex',200)
    print(chq_1)
    chq_1.withdraw(100)
    print(chq_1.transaction())


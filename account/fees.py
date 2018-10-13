class fees:
    def __init__(self, balance:float) -> 'None':
        self.balance = balance
        return

    def over_draft(self,amount:float) -> float:
        self.balance=self.balance - (amount * 1.03)
        return self.balance

    def bounced_cheque(self)->float:
        self.balance = self.balance - 25
        return self.balance

    def below_1000(self)->float:
        self.balance = self.balance - 10
        return self.balance

    def interest(self)->float:
        self.balance = self.balance * 1.02
        return self.balance

# if __name__ == "__main__":
#     # fee_1 = fees(100)
#     # print(fee_1.interest())
#     pass
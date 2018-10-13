from .saving import Savings
class Savings_term(Savings):
    def __init__(self, name:str, balance:float = 0.0):
        super(Savings_term, self).__init__(name,balance)
        return

if __name__ == "__main":
    pass
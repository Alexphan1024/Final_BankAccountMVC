from .saving import Savings
from .chequing import Chequing
from .term_saving import Savings_term

if __name__ == "__main__":
    chq_1 = Chequing('Sally',1000)
    sav_1 = Savings('Joe',5000)
    savt_1 = Savings_term('Sally',7000)
    sav_1.deposit(100)
    print("Joe's New Balance:",sav_1.balance)
    chq_1.withdraw(50)
    savt_1.withdraw(50)
    print('Sally New Balance:{}\n'.format(chq_1.balance))
    chq_1.withdraw(500)
    chq_1.withdraw(450)
    chq_1.bounce_cheque()
    sav_1.below_1000()
    savt_1.below_1000()
    sav_1.change_name('Joseph')
    print(chq_1, '\n')
    print(sav_1, '\n')
    print(savt_1, '\n')
    print("Sally's Chequing Account\n" + chq_1.transaction())
    print("\nJoe's Saving Account\n" + sav_1.transaction())
    print("\nSally's Saving Term Account\n" + savt_1.transaction())


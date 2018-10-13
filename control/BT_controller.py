# from BT_view import *
# from BT_model import *
# from Account_model import *
from model.BT_model import *
from view.BT_view import *
from model.Account_model import *

class BTController:

    def __init__(self):
        self.view = BTView()
        self.BTmodel = BankTellerDB()
        self.Amodel = AccountDB()

    def start(self):
        valid_input = False
        while not valid_input:
            if self.BTmodel.check_teller(self.view.Userlogin(), self.view.Passlogin()):
                while True:
                    option = self.view.option_select()
                    if option == "1":
                        card_num = self.view.user_card()
                        pin_num = self.view.user_pin()
                        while True:
                            self.Amodel.readcsv()
                            if self.Amodel.check_acc(card_num, pin_num):
                                acc = self.view.account_type()
                                id = self.Amodel.search_acc_id(card_num)
                                if acc == "1":
                                    while True:
                                        opt = self.view.account_manage()
                                        acc_num = 3
                                        if opt == "1":
                                            self.Amodel.acc_deposit(id,acc_num,self.view.deposit())

                                        elif opt == "2":
                                            self.Amodel.acc_withdraw(id,acc_num,self.view.withdraw())

                                        elif opt == "3":
                                            self.Amodel.acc_showbalance(id,acc_num)

                                        elif opt == "4":
                                            print("Out of Paper")

                                        else:
                                            break
                                elif acc == "2":
                                    acc_num = 4
                                    while True:
                                        opt = self.view.account_manage()
                                        if opt == "1":
                                            self.Amodel.acc_deposit(id,acc_num,self.view.deposit())

                                        elif opt == "2":
                                            self.Amodel.acc_withdraw(id,acc_num,self.view.withdraw())

                                        elif opt == "3":
                                            self.Amodel.acc_showbalance(id,acc_num)

                                        elif opt == "4":
                                            print("Out of Ink")

                                        else:
                                            break
                                else:
                                    break
                            else:
                                print("\nInvalid Client Credentials")
                                break
                    elif option == "2":
                        self.Amodel.make_acc(self.view.accountmaker())
                    elif option == "3":
                        break
                    else:
                        print("\nInvalid Option")
            else:
                print("\nIncorrect Bank Teller Credentials")

# if __name__ == "__main__":
#     controller = BTController()
#     while True:
#         controller.start()
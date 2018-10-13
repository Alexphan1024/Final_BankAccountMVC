import getpass
import random
import os.path

class BTView:
    def __init__(self):
        self.dicts = {}

    def Userlogin(self):
        return input("\nBank Username: ")

    def Passlogin(self):
        return input("\nPassword: ")

    def option_select(self):
        print("\n--Account Management--")
        print(" 1. Manage Account")
        print(" 2. Create Account")
        print(" 3. Sign Out")
        return input(">>> ")

    def user_card(self):
        return input("\nClient Card Number: ")

    def user_pin(self):
        return input("\nClient PIN Number: ")

    def account_type(self):
        print("\n--Account Type--")
        print(" 1. Chequing Account")
        print(" 2. Saving Account")
        print(" 3. Cancel")
        return input(">>> ")

    def account_manage(self):
        print("\n---Account Options---")
        print("   1. Deposit")
        print("   2. Withdraw")
        print("   3. Show Balance")
        print("   4. Print Receipt")
        print("   5. Cancel")
        return input(">>> ")

    def deposit(self):
        return input("\nDeposit Amount: ")

    def withdraw(self):
        return input("\nWithdraw Amount: ")

    def account_create_name(self):
        x = input("\nClient Full Name: ")
        self.dicts['Name'] = x
        return self.dicts

    def account_create_pin(self):
        return input("\nEnter Pin: ")

    def account_create_balance(self):
        return input("\nBalance: ")

    def accountmaker(self):
        name = input("\nClient Full Name: ")
        while True:
            pin = input("\nEnter Pin: ")
            try:
                if 4 <= len(pin) <= 6 and (int(pin) >= 100000 or int(pin) >= 1000):
                    break
            except ValueError:
                pass

        cbal = input("\nCheque Balance: ")
        dbal = input("\nDeposit Balance: ")
        self.dicts['Name'] = name
        self.dicts['Pin'] = pin
        self.dicts['Cbalance'] = cbal
        self.dicts['Dbalance'] = dbal
        x = random.randint(100000,999999)
        self.dicts['Account#'] = x
        self.dicts['Log'] = str(x)+".txt"
        print("\nSuccess")
        return self.dicts

# print(BTView().accountmaker())



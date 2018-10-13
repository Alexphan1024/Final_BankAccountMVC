from tkinter import *
from view.view_deposit import *
from view.view_balance import *
from view.view_withdraw import *
from view.view_translog import *

class ControlPaymentOptions:
    def __init__(self,payoptpage,acc_menu,loginpage, acc_id, acc_type):
        self.paymenoptionpage = payoptpage
        self.acc_menu = acc_menu
        self.loginpage = loginpage
        self.id = acc_id
        self.type = acc_type

    def sign_out(self):
        self.loginpage.deiconify()
        self.paymenoptionpage.destroy()

    def back(self):
        self.acc_menu.deiconify()
        self.paymenoptionpage.destroy()

    def depositpage(self):
        self.paymenoptionpage.withdraw()
        self.window = Tk()
        DepositWindow(self.window, self.paymenoptionpage, self.id, self.type)


    def withdrawpage(self):
        self.paymenoptionpage.withdraw()
        self.window = Tk()
        WithdrawWindow(self.window, self.paymenoptionpage, self.id, self.type)

    def balancepage(self):
        self.paymenoptionpage.withdraw()
        self.window = Tk()
        Show_Balance(self.window, self.paymenoptionpage, self.id, self.type)

    def tranlogpage(self):
        self.paymenoptionpage.withdraw()
        self.window = Tk()
        Trans_Log(self.window, self.paymenoptionpage, self.id,self.type)


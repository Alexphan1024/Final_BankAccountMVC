from tkinter import *
from view.view_paymentoptions import *

class ControlAccountMenu:

    def __init__(self,accountmenupage,loginpage, acc_id, acc_type):
        self.loginpage = loginpage
        self.account_menu_page = accountmenupage
        self.id = acc_id
        self.type = acc_type

    def win(self):
        self.account_menu_page.withdraw()
        self.window = Toplevel()
        PaymentOptions(self.window, self.account_menu_page,self.loginpage, self.id, self.type)

    def sign_out(self):
        self.loginpage.deiconify()
        self.account_menu_page.destroy()

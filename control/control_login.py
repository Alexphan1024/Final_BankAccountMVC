# from accountmenu import *
from tkinter import messagebox
from tkinter import *
from view.view_accountmenu import *
from model.model_login import *

class Accountoptionpage:
    def __init__(self,parent,acc,pin):
        self.acc = acc
        self.pin = pin
        self.parent = parent
        self.login_check = Model_Login()
        self.r = Read_csv()

    def accountoptionpage(self, id, pin, id_box, pin_box):
        if len(id) == 6 and 4 <= len(pin) <= 6:
            if self.login_check.login_confirmation(id, pin):
                self.clear_box(id_box, pin_box)
                self.r.readcsv()
                self.parent.withdraw()
                self.window = Toplevel()
                x = AccountMenu(self.window, self.parent, id)
                self.r.show_acc_type(id, x)
            else:
                acc_err = "Account Credentials Invalid"
                messagebox.showinfo(title="Login Error", message=acc_err)
                self.clear_box(id_box, pin_box)
        elif len(id) != 6:
            log_err = "Account Number is not 6 digits"
            messagebox.showinfo(title="Login Error", message=log_err)
            self.clear_box(id_box, pin_box)
        elif 4 >= len(pin) or len(pin) >= 6:
            pin_err = "Pin number is not between 4 to 6 digits"
            messagebox.showinfo(title="Pin Error", message=pin_err)
            self.clear_box(id_box, pin_box)


    def clear_box(self, id_box, pin_box):
        id_box.delete(0, "end")
        pin_box.delete(0, "end")


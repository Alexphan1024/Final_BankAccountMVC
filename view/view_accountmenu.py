from tkinter import *
from control.control_accountmenu import *

class AccountMenu:

    def __init__(self, parent, loginpage, acc_id):
        # parent is Tk()
        self.master = parent
        self.loginpage = loginpage
        self.id = acc_id

        #window settings (size/name/background_color)
        self.master.title("Account Options")
        self.master.geometry('600x400')
        self.master.config(background='#0341a5')

        #frames
        self.top_frame = Frame(self.master)
        self.mid_frame = Frame(self.master)
        self.bot_frame = Frame(self.master)

        self.top_frame.grid(column=0, row=0,padx=170, pady= 30)
        self.mid_frame.grid(column=0, row=1,padx=170, pady= 25)
        self.bot_frame.grid(column=0, row=2,padx=170, pady= 30)

        #chequing
        self.chequing_button = Button(self.top_frame, text="Chequing",width=30, height=4,background="#c4dafc",command=ControlAccountMenu(self.master,self.loginpage, self.id, "3").win)
        self.chequing_button.config(font=("Helvetica", 10))
        self.chequing_button.grid(row=0, column=1)

        #saving
        self.saving_button = Button(self.mid_frame, text="Saving", width=30, height=4, background="#c4dafc",command=ControlAccountMenu(self.master,self.loginpage,self.id, "4").win)
        self.saving_button.config(font=("Helvetica", 10))
        self.saving_button.grid(row=0, column=1)

        #LogOut
        self.logout_button = Button(self.bot_frame, text="Sign Out", width=30, height=4, background="#c4dafc", command=ControlAccountMenu(self.master,self.loginpage,self.id, "2").sign_out)
        self.logout_button.config(font=("Helvetica", 10))
        self.logout_button.grid(row=0, column=1)


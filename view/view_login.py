from tkinter import *
from control.control_login import *

class LoginWindow:

    def __init__(self, master):

        self.master = master
        self.master.geometry('600x400')
        self.master.config(background="#0341a5")

        self.master.title("Login")
        self.login_menu = Menu(self.master)

        self.top_frame = Frame(self.master, background="#0341a5")
        self.mid_frame = Frame(self.master, background="#0341a5")
        self.bot_frame = Frame(self.master, background="#0341a5")

        self.top_frame.grid(column=0, row=0, padx=170, pady=30)
        self.mid_frame.grid(column=0, row=1, padx=170, pady=30)
        self.bot_frame.grid(column=0, row=2, padx=170, pady=30)

        self.acc_label = Label(self.top_frame, height=2, width=9, text="Account#", font="Helvetica")
        self.acc = Entry(self.top_frame, width=20)
        self.pin_label = Label(self.mid_frame, height=2, width=9, text="PIN#", font="Helvetica")
        self.pin = Entry(self.mid_frame, width=20, show="*")
        self.enter = Button(self.bot_frame, text="Enter", width=20, height=3, command=lambda:Accountoptionpage(self.master,self.acc.get(), self.pin.get()).accountoptionpage(self.acc.get(), self.pin.get(), self.acc, self.pin), font="Helvetica")


        self.acc_label.grid(row=0, column=0, padx=5, pady=5)
        self.acc.grid(row=0, column=1, padx=5, pady=5)
        self.pin_label.grid(row=0, column=0, padx=5, pady=5)
        self.pin.grid(row=0, column=1, padx=5, pady=5)
        self.enter.grid(row=0, column=0, padx=5, pady=5)


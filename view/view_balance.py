from tkinter import *
from control.control_balance import *
from model.model_readcsv import *

class Show_Balance():
    def __init__(self, master, payoptpage, acc_id, acc_type):
        self.master = master
        self.payoptpage =payoptpage
        self.read = Read_csv()
        self.read1 = self.read.readcsv()
        self.readbalance = self.read.balance(acc_id, acc_type)
        self.master.geometry('600x400')
        self.master.config(background="#0341a5")
        self.id = acc_id
        self.type = acc_type

        self.master.title("Balance")
        self.login_menu = Menu(self.master)

        self.top_frame = Frame(self.master, background="#0341a5")
        self.mid_frame = Frame(self.master, background="#0341a5")
        self.bot_frame = Frame(self.master, background="#0341a5")

        self.top_frame.grid(column=0, row=0, padx=0, pady=10, sticky=W)
        self.mid_frame.grid(column=0, row=1, padx=200, pady=10)
        self.bot_frame.grid(column=0, row=2, padx=200, pady=10)

        self.balance_label = Label(self.mid_frame, height=2, width=9, text="Balance:", font=("Helvetica", 20))
        self.balance_label.grid(row=0, column=0, padx=10, pady=10)
        self.balance_num_label = Label(self.bot_frame, height=2, width=9, text=self.readbalance, font=("Helvetica", 20))
        self.balance_num_label.grid(row=0, column=0, padx=10, pady=10)

        self.back_button = Button(self.top_frame, text="Back", background="#c4dafc", font=("Helvetica", 10), width=4,command=Control_Show_Balance(self.master,self.payoptpage).back)
        self.back_button.grid(padx=10, pady=10)


from tkinter import *
from control.control_deposit import *
from model.model_deposit import *
class DepositWindow:

    def __init__(self, master,payoptpage, acc_id, acc_type):

        self.master = master
        self.payoptpage = payoptpage
        self.master.geometry('600x400')
        self.master.config(background="#0341a5")
        self.id = acc_id
        self.type = acc_type

        self.master.title("Deposit")
        self.login_menu = Menu(self.master)

        self.top_frame = Frame(self.master, background="#0341a5")
        self.mid_frame = Frame(self.master, background="#0341a5")
        self.bot_frame = Frame(self.master, background="#0341a5")

        self.top_frame.grid(column=0, row=0, padx=0, pady=0, sticky=W)
        self.mid_frame.grid(column=0, row=1, padx=0, pady=10)
        self.bot_frame.grid(column=0, row=2, padx=30, pady=10)

        # back button
        self.back_button = Button(self.top_frame, text="Back", background="#c4dafc", font=("Helvetica", 10), width=4,command=ControlDepositWindow(self.master,self.payoptpage).back)
        self.back_button.grid(padx=10,pady=10)

        self.choose_amount_label = Label(self.mid_frame, text='Choose your deposit amount.',font=("Helvetica", 18, 'bold'), background="#0341a5", foreground="White")

        self.choose_amount_label.grid(pady=10)

        self.ohundred_button = Button(self.bot_frame, text ="$100",height=3,width=13, font=("Helvetica", 10), background="#c4dafc",command=lambda:Model_Deposit(self.master,self.payoptpage,self.id,self.type).deposit(100))
        self.thundred_button = Button(self.bot_frame, text ="$200",height=3,width=13, font=("Helvetica", 10), background="#c4dafc",command=lambda:Model_Deposit(self.master,self.payoptpage,self.id,self.type).deposit(200))
        self.fhundred_button = Button(self.bot_frame, text ="$500",height=3,width=13,  font=("Helvetica", 10), background="#c4dafc",command=lambda:Model_Deposit(self.master,self.payoptpage,self.id,self.type).deposit(500))
        self.thousand_button = Button(self.bot_frame, text ="$1000",height=3,width=13, font=("Helvetica", 10), background="#c4dafc",command=lambda:Model_Deposit(self.master,self.payoptpage,self.id,self.type).deposit(1000))

        self.ohundred_button.grid(column=0, padx=10,row=0)
        self.thundred_button.grid(column=1, padx=10,row=0)
        self.fhundred_button.grid(column=2, padx=10,row=0)
        self.thousand_button.grid(column=3, padx=10,row=0)

from tkinter import *
from model.model_readcsv import *
from control.control_paymentoptions import *
class PaymentOptions:
    def __init__(self, parent, acc_menu, loginpage, acc_id, acc_type):
        # parent is Tk()
        self.master = parent
        self.acc_menu = acc_menu
        self.loginpage =loginpage
        self.read = Read_csv()
        self.read1 = self.read.readcsv()
        self.readname = self.read.name(acc_id)
        self.id = acc_id
        self.type = acc_type

        # window settings (size/name/background_color)
        self.master.title("Payment Options")
        self.master.geometry('600x400')
        self.master.config(background='#0341a5')

        #frames
        self.top_frame = Frame(self.master, background="#0341a5")
        self.mid_frame = Frame(self.master, background="#0341a5")
        self.bot_frame = Frame(self.master, background="#0341a5")

        self.top_frame.grid(column=0, row=0,padx=10, pady=10, sticky=W)
        self.mid_frame.grid(column=0, row =1,padx=10, pady=10)
        self.bot_frame.grid(column=0, row=2, padx=10, pady=10,sticky=S+E)

        #back button
        self.back_button = Button(self.top_frame, text="Back", background="#c4dafc",font=("Helvetica", 10), width=4, command=ControlPaymentOptions(self.master,self.acc_menu,self.loginpage, self.id, self.type).back)
        self.back_button.grid(row=0, column=0,padx=(0,145))

        #signout button
        self.signout_button = Button(self.bot_frame, text="Sign Out", background="#c4dafc", font=("Helvetica", 10),command=ControlPaymentOptions(self.master,self.acc_menu,self.loginpage, self.id, self.type).sign_out)
        self.signout_button.grid(row=0, column=0,padx=160, pady=(0,9))

        #payment options

        #deposit button
        self.deposit_button = Button(self.mid_frame, text="Deposit", width=20, height=4,font=("Helvetica", 10), background="#c4dafc",command=ControlPaymentOptions(self.master,self.acc_menu,self.loginpage, self.id, self.type).depositpage)
        self.deposit_button.grid(row=0, column=2,padx=(100,10), pady=10)

        #withdraw button
        self.withdraw_button= Button(self.mid_frame, text="Withdraw", width=20, height=4,font=("Helvetica", 10), background="#c4dafc",command=ControlPaymentOptions(self.master,self.acc_menu,self.loginpage, self.id, self.type).withdrawpage)
        self.withdraw_button.grid(row=0, column=3,padx=10, pady=10)

        #show balance button
        self.balance_button = Button(self.mid_frame, text="Show Balance", width=20, height=4,font=("Helvetica", 10), background="#c4dafc",command=ControlPaymentOptions(self.master,self.acc_menu,self.loginpage, self.id, self.type).balancepage)
        self.balance_button.grid(row=1, column=2,padx=(100,10), pady=10)

        #transaction log button
        self.trans_log= Button(self.mid_frame, text="Transaction Log", width=20, height=4,font=("Helvetica", 10), background="#c4dafc",command=ControlPaymentOptions(self.master,self.acc_menu,self.loginpage, self.id, self.type).tranlogpage)
        self.trans_log.grid(row=1, column=3,padx=10, pady=10)

        #welcome line
        self.welcome_label= Label(self.top_frame, text="Welcome:",background='#0341a5', foreground='White',font=("Helvetica", 15))
        self.welcome_label.grid(row=0,column=1, sticky=N,padx=(0,0))

        '''replace "__name__" with there name or id'''
        self.welcome_name = Label(self.top_frame, text=self.readname,background='#0341a5', foreground='White',font=("Helvetica", 15))
        self.welcome_name.grid(row=0, column=2, sticky=N)

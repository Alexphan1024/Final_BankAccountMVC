from tkinter import *
from model.model_readcsv import *
from control.control_paymentoptions import *
from control.control_tranlog import *
class Trans_Log:
    def __init__(self, parent, payoptpage, acc_id,acc):
        # parent is Tk()
        self.master = parent
        self.payoptpage = payoptpage
        self.id = acc_id
        self.acc = acc

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

        #Trans Log
        self.welcome = Label(self.top_frame, text='Transaction Log', background='#0341a5', foreground='White',
                                  font=("Helvetica", 25))
        self.welcome.grid(row=0, column=2, sticky=N)

        #listbox
        self.text = Text(self.mid_frame,height=15,width=55)
        self.text.grid(row=0, column=2, sticky=N, padx=60)
        try:
            self.text.insert(END,open(str(self.acc)+"_"+str(self.id)+".txt").read())
        except FileNotFoundError:
            self.text.insert(END,'No Transactions')


        #back button
        self.back_button = Button(self.top_frame, text="Back", background="#c4dafc",font=("Helvetica", 10), width=4,command=ControlTranLogWindow(self.master,self.payoptpage).back)
        self.back_button.grid(row=0, column=0,padx=(0,130))

        #print button
        self.print_button = Button(self.bot_frame, text="Print", background="#c4dafc", font=("Helvetica", 10), width=4)
        self.print_button.grid(row=0, column=0,pady=(0,9),sticky=N)


class ControlWithdrawWindow:

    def __init__(self, depositpage, payoptpage):
        self.payoptpage = payoptpage
        self.depositpage = depositpage

    def back(self):
        self.payoptpage.deiconify()
        self.depositpage.destroy()

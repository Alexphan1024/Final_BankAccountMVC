import csv
import os

_BT_FILE = os.path.dirname(__file__) + '\\Bank_Teller.csv'

class BankTellerDB:

    def __init__(self):
        self.info = []
        with open(_BT_FILE, "r") as file:
            reader = csv.reader(file, delimiter=",")
            next(file)
            for row in reader:
                self.info.append(row)

    def check_teller(self,id,pin):
        num = 0
        try:
            if (id == self.info[num][0]) and (pin == self.info[num][1]):
                return True
            else:
                while True:
                    num = num + 1
                    if (id == self.info[num][0]) and (pin == self.info[num][1]):
                        return True
        except IndexError:
            pass



# if __name__ == "__main__":
#     x = BankTellerDB()
#     print(bankteller_info)
#     print(x.check_teller('435870947','101'))
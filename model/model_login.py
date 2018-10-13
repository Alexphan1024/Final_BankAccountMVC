from model.model_readcsv import *
import os

class Model_Login:

    def __init__(self):
        self.r = Read_csv()
        self.r.readcsv()
        self.info = self.r.infomation

    def login_confirmation(self, id, pin):
        num = 0
        try:
            if (id == self.info[num][1]) and (pin == self.info[num][2]):
                return True
            else:
                while True:
                    num = num + 1
                    if (id == self.info[num][1]) and (pin == self.info[num][2]):
                        return True
        except IndexError:
            pass


    def search_acc_id(self, id):
        for lists in self.info:
            if str(id) in lists:
                return (self.info.index(lists), lists.index(id))

    def search_acc_pin(self, pin):
        for lists in self.info:
            if str(pin) in lists:
                return (self.info.index(lists), lists.index(pin))




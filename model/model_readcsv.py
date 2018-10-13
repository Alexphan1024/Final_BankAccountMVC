from account.account import *
import os
import csv
from view.view_accountmenu import *

class Read_csv:
    def __init__(self):
        self._info = []
    def readcsv(self):
        with open(os.path.dirname(__file__) + '\\info.csv', 'r') as file:
            reader = csv.reader(file,delimiter=",")
            next(file)
            for row in reader:
                self._info.append(row)

    def get_info(self):
        return self._info[self.search_acc_id(id)[0]][2]

    @property
    def infomation(self):
        return self._info

    def balance(self, id, type):
        return "$ {}".format(self._info[self.search_acc_id(id)[0]][int(type)])

    def name(self, id):
        return self._info[self.search_acc_id(id)[0]][0]

    def search_acc_id(self, id):
        for lists in self._info:
            if str(id) in lists:
                return self._info.index(lists), lists.index(id)

    def show_acc_type(self, id, i):
        if self._info[self.search_acc_id(id)[0]][3].isdigit() == False :
            i.chequing_button.grid_forget()
        elif self._info[self.search_acc_id(id)[0]][4].isdigit() == False:
            i.saving_button.grid_forget()
        else:
            return
import csv
import os
_ACCOUNT_FILE = os.path.dirname(__file__) + '\\info.csv'

account_info = []

class AccountDB:

    def __init__(self):
        # with open(_ACCOUNT_FILE, "r") as file:
        #     reader = csv.reader(file, delimiter=",")
        #     next(file)
        #     for row in reader:
        #         account_info.append(row)
        pass
    def readcsv(self):
        with open(_ACCOUNT_FILE, "r") as file:
            reader = csv.reader(file, delimiter=",")
            next(file)
            for row in reader:
                account_info.append(row)

    def check_exist(self, i):
        for lists in account_info:
            if str(i) in lists:
                return (account_info.index(lists), lists.index(i))

    def check_acc(self, user_num, user_pin):
        num = 0
        try:
            if (user_num == account_info[num][1]) and (user_pin == account_info[num][2]):
                return True
            else:
                while True:
                    num = num + 1
                    if (user_num == account_info[num][1]) and (user_pin == account_info[num][2]):
                        return True
        except IndexError:
            pass

    def search_acc_id(self, id):
        for lists in account_info:
            if str(id) in lists:
                return account_info.index(lists)

    # def search_acc_pin(self, pin):
    #     for lists in account_info:
    #         if str(pin) in lists:
    #             return (account_info.index(lists), lists.index(pin))

    def acc_deposit(self,id,acc_type, amount):
        try:
            self.readcsv()
            print("Deposit: ${}\nCurrent Balance: ${}".format(amount,int(account_info[id][acc_type]) + int(amount)))
            account_info[id][acc_type] = int(account_info[id][acc_type]) + int(amount)
            with open(os.path.dirname(__file__) + '\\info.csv', 'w+') as updated:
                csv_writer = csv.writer(updated, lineterminator='\n')
                csv_writer.writerow(("Name", "ID", "Pin", "cBalance", "sBalance", "Log"))
                for rows in account_info:
                    csv_writer.writerow(rows)
            # del _ACCOUNT_FILE[:]
        except ValueError:
            if acc_type == 3:
                print('No Chequing Account')
            else:
                print('No Saving Account')




    def acc_withdraw(self,id,acc_type, amount):
        try:
            self.readcsv()
            if int(amount) <= int(account_info[int(id)][acc_type]):
                account_info[int(id)][acc_type] = int(account_info[int(id)][acc_type]) - int(amount)
                print("Withdraw: ${}\nCurrent Balance: ${}".format(amount,account_info[int(id)][acc_type]))
                with open(os.path.dirname(__file__) + '\\info.csv', 'w+') as updated:
                    csv_writer = csv.writer(updated, lineterminator='\n')
                    csv_writer.writerow(("Name", "ID", "Pin", "cBalance", "sBalance", "Log"))
                    for rows in account_info:
                        csv_writer.writerow(rows)
                # del _ACCOUNT_FILE[:]
            else:
                print("\nUnable to withdraw $", amount)
        except ValueError:
            if acc_type == 3:
                print('No Chequing Account')
            else:
                print('No Saving Account')



    def acc_showbalance(self,id,acc_type):
        self.readcsv()
        print("Balance: ${}".format(account_info[int(id)][acc_type]))
        # del _ACCOUNT_FILE[:]

    def make_acc(self,dict):
        with open(_ACCOUNT_FILE, "a+",newline='\n') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow((str(dict.get('Name')),str(dict.get("Account#")),str(dict.get("Pin")),str(dict.get('Cbalance')),str(dict.get('Dbalance')),str(dict.get('Log'))))


# if __name__ == "__main__":
#     x = AccountDB()
    # print(x.acc_deposit(1,4,10))
    # print(x.acc_withdraw(1,4,10))
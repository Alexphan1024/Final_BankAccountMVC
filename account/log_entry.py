class Log:
    def __init__(self):
        self.list = []
        self.dict = {}

    def adds(self,acct_num,time,type,tranaction):
        if str(acct_num) in self.dict:
            self.dict[str(acct_num)] = self.dict.get(str(acct_num))+ "\n" + str(time) + str(type) + str(tranaction)
        else:
            self.dict[str(acct_num)] = str(time) + str(type) + str(tranaction)
        return

    def shows_transaction(self,acct_num):
      return ('Transaction Log:\n') + self.dict[str(acct_num)]


if __name__ == "__main__":
    log = Log()
    log.adds("a",'11:30', " deposit: $" , 20)
    log.adds("a",'11:30', " deposits: $" , 20)
    log.adds("b",'11:30', " deposits: $" , 200)
    log.adds("b",'11:30', " deposits: $" , 2005)
    print(log.shows_transaction('b'))

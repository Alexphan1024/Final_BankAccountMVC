from time import localtime, strftime
class Log:
    def __init__(self):
        self.list = []
        self.dict = {}

    def adds(self,acct_num,type,tranaction,acc_type):
        if str(acct_num) in self.dict:
            self.dict[str(acct_num)] = self.dict.get(str(acct_num)) + "\n" + strftime("%Y-%m-%d %H:%M:%S",
                                                                                      localtime())+ " " + str(type) + str(
                tranaction+ "\n")
            file = open(str(acc_type)+"_"+str(acct_num) + ".txt", "a+")
            file.write(self.dict[str(acct_num)])
            file.close()
        else:
            self.dict[str(acct_num)] = strftime("%Y-%m-%d %H:%M:%S", localtime())+ " " + str(type) + str(tranaction)+ "\n"
            file = open(str(acc_type)+"_"+str(acct_num)+".txt","a+")
            file.write(self.dict[str(acct_num)])
            file.close()
        return

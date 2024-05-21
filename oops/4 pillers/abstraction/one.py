from ABC import *

class Account(ABC):
    @abstractmethod
    def cal_bal(self):
        pass

class SA(Account):
    def cal_bal(self):
        print("calculating balance")

class CA(Account):
    pass

a1=Account()                   
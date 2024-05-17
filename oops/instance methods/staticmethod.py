class Account:
    @staticmethod
    def cal_intrest(p,r,t):
        return p*r*t/100

print(Account.cal_intrest(100000,2,3))        

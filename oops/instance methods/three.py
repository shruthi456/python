class Account:
    noObject=0
    def __init__(self):
        Account.noObject=Account.noObject + 1

    @classmethod
    def get_noofobjects(cls):
        return cls.noObjects    

a1=Account()
a2=Account()
a3=Account()
a4=Account()    
print(Account.noObject)
print(Account.get_noofobjects)   
class Account:
    noObject=0
    def __init__(self):
        Account.noObject=Account.noObject + 1

a1=Account()
a2=Account()
a3=Account()
a4=Account()    
print(Account.noObject)    
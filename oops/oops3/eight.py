class Account:
    min_bal=5000
    def __init__(self,id,name,email,amount):
        self.acc_id=id
        self.acc_name=name
        self.acc_email=email
        self.acc_bal=amount

    def open_Account(self):
        print("Account opened successfully")

    def deposit_amount(self,amount):
        self.acc_bal=self.acc_bal + amount 

    def withdrawl(self,amount):
        self.acc_bal = self.acc_bal - amount 

    def get_bal(self):
        return self.acc_bal          

a1=Account(101,"Rahul",'rahul@gmail.com',4000)       
print(a1.__dict__)
a1.deposit_amount(10000)
a1.deposit_amount(10000)
print(a1.__dict__)
a1.withdrawl(15)
print(a1.__dict__)


print(a1.get_bal())
print(a1.get_bal())
print(a1.get_bal())
print(a1.get_bal())
print(a1.get_bal())


a1.branch_name = 'Banglore';
print(a1.__dict__)
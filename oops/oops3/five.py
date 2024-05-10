class Account:
    def __init__(self,id,name,email,amount):
        self.acc_id=id
        self.acc_name=name
        self.acc_email=email
        self.acc_amount=amount

    def open_Account(self):
        print("Account opened successfully")

    def deposit_Account(self,amount):
        print("Amount Deposited Succesfully")

a1=Account(101,"Rahul",'rahul@gmail.com',4000)     
a2=Account(102,"Sonia",'sonia@gmail.com',5000)        
a3=Account(103,"Priyanka",'priya@gmail.com',6000)  
print(a1.__dict__)
print(a2.__dict__)
print(a3.__dict__)
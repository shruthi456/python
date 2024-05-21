from Account import Account

class CA(Account):
    min_bal=25000
    def__init__(self,id.name,email,address,amount):
        super().__init__(name,email,address)
        self.acc_id=id
        self.acc_bal=amount
    def set_mobile_no(self,mobile):
        set.mobile=mobile

    def get_mobile_no(self):
        return self.mobile
    def cal_bal(self):
        return self.acc_bal-self.min_bal
ca1=CA(201,'Priya','priya@gmail.com','chennai',7000)
print(ca1.__dict__)
print(ca1.cal_bal())                
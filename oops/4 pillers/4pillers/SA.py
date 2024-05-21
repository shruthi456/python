from Account import Account


class SA(Account):
    min_bal=500
    def__init__(self,id,name,email,address,amount):
        self.acc_id=id
        self.acc_bal=amount

    def cal_bal(self):
        return self.acc_bal-self.min_bal

sa1=SA(101,'Rahul','rahu@gmail.com','Bangalore',6000)
print(sa1.__dict__)
print(sa1.cal_bal())
sa1.set_mobile_no(9879876540)
print(sa1.get_mobile_no())            
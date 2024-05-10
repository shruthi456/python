class Account:
    def open_Account(self):
        print(id(self))

    def deposit_Account(self,amount):
        self.acc_bal = amount

a1=Account()
a1.open_Account()
a1.deposit_Account(5000)

print(id(a1))
print(a1.__dict__)
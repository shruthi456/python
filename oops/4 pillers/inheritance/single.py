class parent:
    def m1(self):
        print("parent class m1 -instance method")
    
    def m2(self):
        print("parent class m2 -instance method")    
class child(parent):
    def m3(self):
        print("child class m3 -instance method")
c1=child()
c1.m1()
c1.m2()
c1.m3()
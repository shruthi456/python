class parent1:
    def m1(self):
        print("parent class m1 -instance method")
class parent2:    
    def m1(self):
        print("parent class m1 -instance method")    
class child(parent1,parent2):
    def m2(self):
        print("child class m2 -instance method")
c1=child()
c1.m1()
c1.m2()

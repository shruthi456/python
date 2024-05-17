class parent:
    def m1(self):
        print("parent class m1 -instance method")
class child1(parent):    
    def m2(self):
        print("childclass m2 -instance method")    
class child2(parent):
    def m3(self):
        print("child2 class m3 -instance method")
c1=child1()
c2=child2()
c1.m1()
c1.m2()
#c1.m3()
c2.m1()
c2.m3()

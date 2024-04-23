def outer():
    print("outer function")
def inner1():
    print("inner function")
inner1()

def inner2():
    print("inner function")
inner2()

outer()
inner1() 
inner2()
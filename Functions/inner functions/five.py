def outer():
    print("outer function")
    def inner():
        print("inner function")
    return inner   

inner=outer()
a=inner()
print(a)     
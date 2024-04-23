def outer():
    print("Outer function")
    def inner():
        print("inner function")
    return 100
result=outer()
print(result)

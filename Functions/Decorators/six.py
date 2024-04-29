def smart_div(func):
    pass

    def inner(a,b):
        if b==0:
            print("Can't Divide by Zero")
        else:
            return func(a,b)

    return inner


@smart_div
def calc(a,b):
    print(a/b)


calc(10,1)  #10.0
calc(10,0)  #cant divide by zero
calc(10,2)  #5.0
calc(200,0) #cant divide by zero
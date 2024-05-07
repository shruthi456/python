try:
    print(a)

except ZeroDivisionError as err:
    print(err)
except TypeError as err:
    print(err)
except FileNotFoundError as err:
    print(err)
except:
    print("Variable is Not Found")                
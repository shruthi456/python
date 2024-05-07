try:
    print(10/"ten")

except ZeroDivisionError as err:
    print(10/1)
except TypeError as err:
    print(10/10)
except FileNotFoundError as err:
    print(err)
except:
    print("Variable is Not Found")
#without error handling
fp=open('xyz.txt','r')
data=fp.read()
print(data)
print("Reading file successfully")
fp.close()
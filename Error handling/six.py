fp=None

try:
    fp=open('data.txt','r')
except:
    fp=open('abc.txt','r')


abc = fp.read()
print(abc)
print("Reading Successfully")
fp.close()
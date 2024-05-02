#read data.txt file and print content in terminal/console

fp=open('data.txt','r')
#data=fp.read()
#data=fp.readline()
#data=fp.read(12)
data=fp.readlines()
print(data)

fp.close()
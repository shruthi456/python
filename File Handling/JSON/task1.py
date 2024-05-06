import json
fp1=open('user.json','r')
users=json.load(fp1)
print(type(users))
print(len(users))
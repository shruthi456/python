#read data.csv file and print data
import csv
fp=open('data.csv','r')
user_csv_obj=csv.reader(fp)
users=list(user_csv_obj)

for user in users:
    for data in user:
        print(data,end="\t")
    print()
fp.close        
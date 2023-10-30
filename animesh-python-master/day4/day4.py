# read using of csv
'''
import csv
with open('/home/ubuntu/pyt/data.csv','r')as file_to_read:
    data=csv.reader(file_to_read)
    for i in data:
        print(i)
       '''
#read in csv ,os including path
'''
import csv,os
path='/home/ubuntu/pyt'
os.chdir(path)
with open('data.csv','r')as file_to_read:
    data=csv.reader(file_to_read)
    for i in data:
        print(i)
        '''
#writing to csv (heading)

import csv,os
path='/home/ubuntu/pyt'
os.chdir(path)
feilds = ['Name','occupation','Mode of payment','Destination']

with open('spends.csv','w') as file_to_write:
    exec = csv.writer(file_to_write)
    exec.writerow(feilds)
with open('spends.csv', 'r') as file_to_read:
        data = csv.reader(file_to_read)
        for i in data:
            print(i)

##writing to csv (rows)
import csv,os
path='/home/ubuntu/pyt'
os.chdir(path)
feilds = ['Name','occupation','Mode of payment','Destination']
recs = [
    ['jack','businessmen','credit card', 'croma'],
    ['som', 'self','upi','amazon']
]

with open('spends.csv','w') as file_to_write:
    exec = csv.writer(file_to_write)
    exec.writerow(feilds)
    exec.writerows(recs)
with open('spends.csv', 'r') as file_to_read:
        data = csv.reader(file_to_read)
        for i in data:
            print(i)








#reading some input user-
'''
open(myfile.txt,r)
'''
#----------------------------

#including path-
'''
pystore=open('/home/ubuntu/pyt/scr.py','r')
print(pystore)
'''
#-----------------------------------

#print the path-
'''
pystore=open('/home/ubuntu/pyt/scr.py','r')
sentence=pystore.readline()
print(sentence)
'''
#------------------------------------------

# using while loop for printing all value in file-
'''
pystore=open('/home/ubuntu/pyt/scr.py','r')
sentence=pystore.readline()
while(sentence != ""):
print(sentence)
'''
#----------------------------------

#updating the value in while loop
'''
pystore=open('/home/ubuntu/pyt/scr.py','r')
sentence=pystore.readline()

while(sentence != ""):
  print(sentence)
  sentence = pystore.readline()
  '''
#Not printing the first value.
'''
pystore=open('/home/ubuntu/pyt/scr.py','r')
sentence=pystore.readline()

while(sentence != ""):
 sentence = pystore.readline()
 print(sentence)
 ,,,
 '''
# append
'''
pystore=open('/home/ubuntu/pyt/scr.py','r')
sentence=pystore.readline()
collect=[]

while(sentence != ""):
 print(sentence)
 collect.append(sentence)
 sentence = pystore.readline()
print(collect)

'''
# creating a new file and feching details
'''
pystore=open('/home/ubuntu/pyt/cloned.txt','r')
sentence=pystore.readline()
collect=[]

while(sentence != ""):
 print(sentence)
 collect.append(sentence)
 sentence = pystore.readline()
print(collect)
'''
#writing on file
'''
pystore=open('/home/ubuntu/pyt/cloned.txt','w')
pystore.write('replace the existing content')
pystore.close()

pystore=open('/home/ubuntu/pyt/cloned.txt','r')
line1=pystore.readline()
print(line1)
'''
#read and write
'''
pystore=open('/home/ubuntu/pyt/cloned.txt','r')
line1=pystore.readline()
print(line1)

pystore=open('/home/ubuntu/pyt/cloned.txt','w')
pystore.write('replace the existing content uuu')
pystore.close()

pystore=open('/home/ubuntu/pyt/cloned.txt','r')
line1=pystore.readline()
print(line1)
'''
#by using while loop
'''
pystore=open('/home/ubuntu/pyt/cloned.txt','a')
pystore.write('\n replace the existing content uuu! \n')
pystore.close()
pystore=open('/home/ubuntu/pyt/cloned.txt','r')
sentence=pystore.readline()
while (sentence!=""):
    print(sentence)
    sentence=pystore.readline()
    '''
#
'''

pystore=open('/home/ubuntu/pyt/cloned.txt','r')
full=pystore.read()
print(full)
'''
#
'''
pystore=open('/home/ubuntu/pyt/cloned.txt','r')
full=pystore.read()
for i in full:
 print(i)
 '''
 # read line
'''
pystore = open('/home/ubuntu/pyt/cloned.txt', 'r')
full = pystore.readline()

for i in full:
    print(i)
'''
# find length
'''
pystore = open('/home/ubuntu/pyt/cloned.txt', 'r')
full=pystore.read()
print(len(full))
'''
#
'''''
pystore = open('/home/ubuntu/pyt/cloned.txt', 'r')
full=pystore.readline()
print(full)
'''
# How to Count
'''
pystore = open('/home/ubuntu/pyt/cloned.txt', 'r')
count=0
for i in pystore:
    count+=1
print (count)
print(type(pystore))
'''
# find starting letter
'''
pystore = open('/home/ubuntu/pyt/cloned.txt', 'r')
count = 0

for i in pystore:
    if i.startswith("ghhg"):
    count += 1
        print(i)
        

    else:
     print("no matching", count)

'''
# find any letter
'''
pystore = open('/home/ubuntu/pyt/cloned.txt', 'r')
count = 0
for i in pystore:
    if 'replace' in i:
        count += 1
        print('keyword found in line', count, i)

'''
# rstrip (for removing space)
'''
pystore = open('/home/ubuntu/pyt/cloned.txt', 'r')
count = 0
for i in pystore:
    if 'replace' in i:
        count += 1
        i=i.rstrip()
        print('keyword found in line', count, i)
        '''
# import os
import os
path='/home/ubuntu/pyt/'
os.chdir(path)

print(os.listdir(path))

user_in=input('Enter a file name: ')
pystore=open(user_in,'r')

















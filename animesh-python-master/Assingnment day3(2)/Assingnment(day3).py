#Get input from user for filename to search
#Get additional input from user about what they want: get total count of lines  or get mathing lines with a particular value
#Display output

import os

path = '/home/ubuntu/pyt/'
os.chdir(path)

print(os.listdir(path))

Employee_in = input('Enter a file name: ')
add_input = input('What information do you need from the file? 1: Total count  2: Matching lines: ')

if add_input == '1':
    pystore=open(Employee_in,'r')
    full = pystore.readlines()
    total_lines = len(full)
    print("Total lines on your page:", total_lines)

elif add_input == '2':
    pystore = open(Employee_in,'r')
    count = 0
    for i, line in enumerate(pystore, 1):
        if 'replace' in line:
            count += 1
            line = line.rstrip()
            print("Keyword found in line" ,(count),(line))
        else:
            print("No matching", (count), (line))
else:
            print("invalid option")







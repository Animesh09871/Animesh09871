


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
'''
num1 = ("1,2,3 ")
num2 = ("1,2,3")
num3 = ("4,5,5")

if num1 == num2:
 print(num1,"It's a match!",num2)
elif num2 == num3:
 print(num2,"It's a match!",num3)
 elif num1 == num3:
 print(num2,"It's a match!",num3)
else:
 print(" not a match!") '''

'''

dict1 = {'dhoni': 7, 'sachin': 1, 'kohli': 3}
dict2 = {'dhoni': 7, 'sachin': 1, 'kohli': 3}

if dict1 == dict2:
    print("Dictionaries have same content which is:")
    print(dict1)
else:
    print("Not similar")'''

def square_and_cube(number):
    square = number ** 2
    cube = number ** 3
    print({square})
    print({cube})
number = 14
square_and_cube(number)

def square_and_cube(number):
    square = number ** 1/2
    cube = number ** 1/3
    print({square})
    print({cube})
number = 9
square_and_cube(number)

scores = {'rohit': 90, 'vishal': 78, 'jack': 79, 'jenny': 75}

for name, score in scores.items():
    if score > 78:
        print(name)
    else:
        print(f"{name} did not score higher than 78")





#Create two dictionaries.
#Compare them with each other and display output as “Dictionaries have same content which is” xyz
#Otherwise display, “Not similar”
'''
dict1 = {'dhoni': 7, 'sachin': 1, 'kohli': 3}
dict2 = {'dhoni': 7, 'sachin': 1, 'kohli': 3}

if dict1 == dict2:
    print("Dictionaries have same content which is:")
    print(dict1)
else:
    print("Not similar")'''

#Create a python function to take three numbers as input, comapre them with each other.
#If a number matches with another, display number1 matches with number 2 and similar for other comparison
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



#Create a python function to display the square and cube of a given number.
'''
def square_and_cube(number):
    square = number ** 2
    cube = number ** 3
    print({square})
    print({cube})
number = 14
square_and_cube(number)
'''

#Create a python function to display the squareroot of a given number.
'''
def square_and_cube(number):
    square = number ** 1/2
    cube = number ** 1/3
    print({square})
    print({cube})
number = 9
square_and_cube(number)
'''
#Create dummy dictionary with scores
#Print x has been awarded distinction class (if score is above 80)
#Print x has been awarded first class if score is above 65 and below 80
#Print x has just passed if score is below 65

scores = {'rohit': 90, 'vishal': 78, 'jack': 79, 'jenny': 75}

for name, score in scores.items():
    if score > 78:
        print(name)
    else:
        print(f"{name} did not score higher than 78")


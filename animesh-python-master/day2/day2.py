
def square_and_cube(number):
    square = number ** 2
    cube = number ** 3
    print({square})
    print({cube})
number = 9
square_and_cube(number)

#second way

list = [1,2,3,4,5]

def square_and_cube(n):
 print(n*n)
 print(n*n*n)

for i in list:
     square_and_cube(i)


#map
random = [1,2,3,4,5]

def sq_fn(n):
    print(n*n)
squares=(list(map(sq_fn,random)))

# map cube
random = [1,2,3,4,5]

def sq_fn(n):
    print(n*n*n)
squares=(list(map(sq_fn,random)))



#filter function
school = {"Alice": 90, "Bob": 75, "Charlie": 60, "David": 82, "Eve": 45}
filtered_scores = dict(filter(lambda x: x[1] >= 80, school.items()))

for student, score in filtered_scores.items():
    print(f" highest{student}: {score}")
else:
 filtered_scores = dict(filter(lambda x: x[1] <=80, school.items()))
print(f" lowesr{student}: {score}")

#lamda funtion

sq_fn = lambda n : print(n*n,)
#invoke
sq_fn(5)
#add with lambda
sq_fn = lambda n,y: print(n+y,)
#invoke
sq_fn(5,8)

#lambda

scores=[ 80,90,89,76,0]

gfh = lambda x:x>80

highest=list(filter(gfh,scores))
print(highest)

#lambda with if

scores=[ 80,90,89,76,0]

gfh = lambda x:print(x) if (x>80) else None

highest=list(filter(gfh,scores))
print(highest)

#lambda with else if

scores=[ 80,90,89,76,0]

gfh = lambda x:print(x) if (x>80) else {print(x, 'has top class') if (60< x <80) else None}

highest=list(filter(gfh,scores))
print(highest)


 #putting input
val1 = int(input ('Enter the first number : '))
val2 = int(input ('enter the second number : '))
sum = val1+val2
print(sum)


# chat box

# Name= str(input('Enter your name: '))
# print('Hello', Name.capitalize(),'!')

num1 = int(input("Enter the first num: "))
num2 = int(input("Enter the second num: "))
operation = input("What operation would you like to perform (+, - , *): ")

gfh = lambda num1, num2, operation: (num1 + num2) if operation == '+' else (num1 - num2) if operation == '-' else (num1 * num2) if operation == '*' else None

result = gfh(num1, num2, operation)

print("Result:", result)


v1 = int(input ('Enter a number : '))
v2 = int(input('enter a number'))
method = ('what you need to do: ')

if method.lower() == 'div':
    try:
        div = v1 / v2
    except ZeroDivisionError:
        print("Division by zero error")
    except Exception as e:
        print("An error occurred:", e)
        

pystore=open('/home/ubuntu/pyt/cloned.txt','r')
sentence=pystore.readline()
collect=[]
while(sentence != ""):
 print(sentence)
 collect.append(sentence)
 sentence = pystore.readline()

 print(collect)

 pystore = open('/home/ubuntu/pyt/cloned.txt', 'a')
 pystore.write('replace the existing stuff peter!')
 pystore.close()

 pystore = open('/home/ubuntu/pyt/cloned.txt', 'r')
 line1=psy.readline()
 print(line1)


















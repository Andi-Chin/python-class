print('hello world')

print('your name')

#this is a comment, this will be ignored by the interpreter
# (program executing your code)

#basic data types:
#string, it's just another way of saying words
#you've alreay seen this, you can print it to the console
print('some words')


# numbers!
#these are also a data type
#eg:
1
100
399
4.89
-2
# theses can also be printed to the console
print(900)

#you can also do operations
#eg:
3 * 4
5 / 6
#exponetiation
2 ** 3

print(100 + 200)

#this will not work like you think it would,
#in python, the '^' sign is a xor bit operator, not an exponentiation operator
# the exact process is a bit complicated and will be explained later
print(6 ^ 10) 


#variables:
#they are useful for storing information
#example:
x = 100
#here 'x' is the name of the variable, 100 is the value of it
print(x)
y = 2
print(y)
print(x + y)


#more data types:

shoppingList = ['apple', 'orange', 'cookie']
print(shoppingList)

print(shoppingList[0])

shoppingList[0] = 'milk'
print(shoppingList)

shoppingList.append('juice')
print(shoppingList)


#boolean
True
False

#this is the computer's logic

#you have to use two equals signs to compare them
print(1 == 1)  # this is true
print('hi' == 'hi')  # this is also true
print(20 == 0)	#this is false
print(4 != 3)  # this is true, because 4 is not equal to 3

# you can also assign boolean values to variables
myBool = True


# if statements are a way to control the flow of your code
# the indented after the if statement will only be executed if the expression 
# inside the if evaluated to true

# here, since 1 is equal to 1, the print statement is executed
if 1 == 1:
	print('1 is equal to 1')

# here, since the variable myBool is true, the print statement is executed
if myBool:
	print('myBool is True')


# what if you want to check more complicated cases?
#logical operators
# you can use logical operators to extend boolean evaluations
if 1 == 1 and 2 == 2:
	print('1 is 1 and 2 is 2')


#else blocks
#these are the statements that can come after the if statement
#these will be executed only when the if statement did not evaluate to true

if 1 == 0:
	print('1 is 0')
else:
	print('1 is not 0')

#elif
#this will tested next when the if statement did not evaluate to true
#if this did not evaluate to true either, the else statement will be executed

if 2 == 3:
	print('2 is 3')
elif 5 == 5:
	print('5 is 5')
else:
	print('2 is not 3 and 5 is not 5')

#ever wondered how computers are able to automate things?
# loops!
#say you want to print 'hello world' 10 times
#without using loops, you would have to copy and paste and paste and paste 
#and paste and paste and paste and paste and paste and paste and paste 
#but with loops, you can do it in just a few lines of code!
#we'll start off by learning one type of loop, the for loop
#example:
for iteration in range(10):
	print('hello world!')

#and there it is!
#explanation:
#the variable 'iteration' is what is called a loop counter
#this is the thing that will be incremented until it reaches 10
#the code 'in range(10)' basically tells the computer to increment the
#variable 'iteration' until it reaches ten
# and for each incrementation, 'hello world!' will be printed
# congrats! You've just learned how to use a simple for loop

#now, here are some extra stuff about loops
#since the variable 'iteration' is so long an tedious to type,
#programmers usually just call it 'i'
#the conventional way to write a for loop:
for i in range(10):
	print('hello')

#and since 'i' is incremented each time, let's try printing it
for i in range(10):
	print(i)
#here, we can see starts at 0 and goes up to 9
#that's because in python, 




#string concatenation

myString = 'hello ' + ':)'

print(myString)

# wrong = 'hi ' + 1

right = 'hi ' + str(18)

# casting

print(int('123'))
print(list('asd'))
print(float('3.4'))
print(str(True))

#dictionaries

myDic = {
	'apple': 3,
	'orange': 5,
	'juice': 6
}
print(myDic['juice'])

#functions

def printHi():
	print('hi')

def addTwo(x):
	x += 2

def quadratic(x):
	return x ** 2 + x + 1

#modules

import random
print(random.randint(0, 10))

import math
print(math.pi)

#classes

class Car():
	brand = 'volvo'
	color = 'black'
	price = 10000

print(Car.brand)
print(Car)

Car.name = 'myCar'
print(Car.name)

class Human():
	name = 'Jeff'
	age = 10

	def eat():
		print('i am eating')
	
	def run():
		print("i'm running")
	
	def grow():
		Human.age += 1
print(Human.name, Human.age)
Human.eat()

Human.grow()
print(Human.age)


#instant classes
class Car():
	def __init__(self, brand, color, price, name):
		self.brand = brand
		self.color = color
		self.price = price
		self.name = name
	def drive(self):
		print(self.name + ' is driving!')
	def printPrice(self):
		print(self.price)
volvo = Car('volvo', 'red', 200, 'Tim')
print(volvo.__dict__)

honda = Car('honda', 'silver', 300, 'Jerry')

print(honda.brand)
print(honda.color)
print(honda.price)
print(honda.name)



#more logical operators

1 == 2
2 != 3
True and False
True or False
(False and False) or True
(1 != 2) and (3 == 4)

day = 'wed'

if day == 'sat' or day == 'sun':
	print('it is the weekend')
else:
	print('time for school')


#loop iteration

for element in [1, 2, 3, 4]:
	print(element)

lis = [4, 10, 8, 7]
for index in range(len(lis)):
	lis[index] += 1

print(lis)

#list comprehension
lis = [i for i in range(10)]
print(lis)

hi = [[i for i in range(3)] for j in range(5)]

print(hi)

#the end
#that's basically all the python there is. I think...

#regex

import re

string = 'hello world!'
pattern = 'hello'

pattern = 'h.ello'
pattern = 'h.+world'
pattern = 'h[a-e].+'
pattern = '^.{3}'

print(re.findall(pattern, string))

#and that's regex...







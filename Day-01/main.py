print("Day 1: 100 days of Python Started!")
print("Hello world")
print("Rajat Singh")  
import pandas as pd
print("Pandas version :",pd.__version__)
#My first program
name = "Rajat singh gaur"
age = 17
college = "Maharishi university of information technology"
print("Hello",name,age,college)
#Learning back slash n
print("Hey I am a good boy\nand this viewer is also a good boy/girl")
#Multi line comment
'''
Hii Rajat,What are you doing?
'''
#Escape sequence character
print("Hii\tSir")
print("Hii\n Sir")
#Separator cgaracter
print("Hey",6,7 ,sep = "~")
#Data types and variables
a =1 
b = "Harry brokes"
c = True
d = None
e = 5.6
f = complex(4,6)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(f) 
#operators
#Arithmetic operators
x = 2
y = 4
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)#It will make disapper 0.5
print(x ** y)
print(x % y)  
#End of day one with one exercise question...
#Create a calculator
m = int(input("Number 1:"))
n = int(input("Number 2:"))
print("Calculating all the values----")
print("Addition", m + n)
print("Subtraction", m - n)
print("Multiplication", m * n)
print("Divide", m / n)
#It may be updated further bec one error is created if user entered n = 0
#Again creating a calculator:
p = int(input("No .1:"))
q = int(input("No .2:"))
print("Our values are being calculated")
print("Addition:", p + q)
print("Subtraction:", p - q)
print("Multiplication:", p * q)
if q == 0:
    print("Cannot be divided by 0")
else:
    print("Divide:", p / q)
 
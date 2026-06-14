#Short Hand If else:
a = 330
b = 465
print("A") if a > b else print("+") if a==b else print("B")#B
c = 9 if a < b else 0
print(c)
#We should not use this in complex projects because it ruins the readability of code...
#Enumerate function--It gives us index and values at a same time in sequence
marks = [23,45,67,54,98,62,49,89,90]
index = 0
for mark in marks:
    print(mark)
    if index == 4:
        print("Rajat, Awesome!")
    index += 1    #It is a long way  now time to make them easy...
marks = [23,45,67,54,98,62,49,89,90]
index = 0
for mark in marks:
    print(mark)
    if index == 4:
        print("Rajat, Awesome!")
    index += 1
marks1 = [23,45,67,54,98,62,49,89,90]
for index, mark in enumerate(marks):
    print(mark)
    if index == 4:
        print("Rajat, Awesome!")
#Another example
fruits = ["apple","Mango","orange","Grapes","Litchi"]
for index, fruit in enumerate(fruits):
    print(index , fruit)
#Changing the start index:
fruits1 = ["apple","Banana","Guava","Mango","orange","Grapes","Litchi"]
for index, fruit in enumerate(fruits1 , start=1):
    print(index , fruit)
#How Import in Python works:
from math import sqrt,pi

result = sqrt(9)*pi
print(result)
import math
print(dir(math))
import random
print(dir(random))
print(math.pi,type(math.pi))#3.14 (Float)

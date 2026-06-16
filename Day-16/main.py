#File I/O 
#READING A FILE
f = open("C:\\Users\\ishaw\\OneDrive\\Documents\\GitHub\\100-days-of-Python\Day-16\Python.txt","r")
text = f.read()
print(text)
f.close() 
# X mode - This Mode creates a file and gives an error if the file already exists.
f = open("C:\\Users\\ishaw\\OneDrive\\Documents\\GitHub\\100-days-of-Python\Day-16\Python.txt","rb") #Binary mode
text = f.read()
print(text)
f.close()
# WRITING A FILE
f = open("C:\\Users\\ishaw\\OneDrive\\Documents\\GitHub\\100-days-of-Python\Day-16\Python.txt","w")
text = f.write("Hello World!!!")
print(text)
# Appending to a file.
f = open("C:\\Users\\ishaw\\OneDrive\\Documents\\GitHub\\100-days-of-Python\Day-16\Python.txt","a")
f.write("Hii Siri How are you?")
f.close()
# Using Of with open Statements:
with open("C:\\Users\\ishaw\\OneDrive\\Documents\\GitHub\\100-days-of-Python\Day-16\Python.txt","r") as f:
    text = f.read()
    print(text)
with open("C:\\Users\\ishaw\\OneDrive\\Documents\\GitHub\\100-days-of-Python\Day-16\Python.txt","a") as f:
    f.write("hey I am Inside this")
# Writeline Method:
lines = ["Hello, World!\n", "Python is great!\n", "Let's write to a file.\n"]
with open("C:\\Users\\ishaw\\OneDrive\\Documents\\GitHub\\100-days-of-Python\Day-16\Python.txt", "w") as file:
   file.writelines(lines)
# Seek Function - It allows you to read from any character in your file
f = open("C:\\Users\\ishaw\\OneDrive\\Documents\\GitHub\\100-days-of-Python\Day-16\Python.txt", "r")
f.seek(10) #Skip 10 Character and then read
print(f.read())
f.close()
# Tell Function
f = open("C:\\Users\\ishaw\\OneDrive\\Documents\\GitHub\\100-days-of-Python\Day-16\Python.txt", "r")
f.seek(10) 
print(f.read())
print(f.tell())
f.close()

# Lamba Function
square = lambda x: x*2
cube = lambda x:x*x*x
avg = lambda x,y,z: (x + y + z)/3
print(square(5))
print(cube(5))
print(avg(2,4,6))
def fx(func):
    return 6 + func(2,4,6)
print(fx(lambda x,y,z: (x + y + z)/3))
# MAP   map(function, iterable)
def cube(x):
    return x*x*x

l = [1,2,3,4,5,6,7,8,9]
newl = list(map(cube, l))
print(newl)
# Also we pass lambda function
new = list(map(lambda x:x*2,l))
print(new)

# FILTER
def filter_function(a):
    return a > 4
l = [1,2,3,4,5,6,7,8,9]
newnewl = list(filter(filter_function,l))
print(newnewl) #[5,6,7,8]
# We pass Lambda Function in filter also.
new1 = list(filter(lambda a : a> 4,l))
print(new1)

# REDUCE 
from functools import reduce
numbers = [1,2,3,4,5,6,7,8,9]#45
# How this Function works
# numbers = [3,3,4,5,6,7,8,9]
# numbers = [6,4,5,6,7,8,9]
# numbers = [10,5,6,7,8,9]
# numbers = [15,6,7,8,9]
# numbers = [21,7,8,9]
# numbers = [28,8,9]
# numbers = [36,9]
# numbers = [45]
sum = reduce(lambda x , y: x + y,numbers)
print(sum)
# All Three are High Order Function
 
# 'is' Vs '=='
#Both are comparasion operator
a = 20
b = "20"
print(a is b) # It compare exact location in memory (When identity is same)
print(a == b) # It compare value
c = [2,4,6]
d = [2,4,6]
print(c is d) #False(Different list, List is mutable)
print(c == d) #True
e = 3
f = 3
print(e is f) #True(3 is a constant value that never chnaged)
print(e == f) #True
x = "Rajat"
y = "Rajat"
print(x is y)
print( x==y )
#Same for tuple because tuple is also not changed later tuple is immutable


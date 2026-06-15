#if __name__=="__main__" in Python
def greet():
    print("Hi Rajat Singh ")
if __name__=="__main__" :
    greet()
name = "Rajat"
name2 = "Singh"
sum = name + name2
print(sum) #It will be show..
#OS Module
import os 
cwd = os.getcwd() 
print("Current working directory:", cwd)
import os
print(os.name)
#Local And global variables...
x = 4 #Global variable
print(x)

def hello():
    x = 5 #Local variable
    y = 3
    print(f"The Local x is {x}")
    print(f"The local y is {y}")
    print("Hello My Jackson")

hello()
#Local variables destroyn when function returns,But global variables always present in function.
print(f"The Global x is {x}") 
#print(y)#This will cause an error because y is a local variable and is not accessible outside of the function
#We also chnage the global variable
a = 10
print(a)
def Not():
    global a
    a = 20
    b = 30
    print(f"The local a is {a}")
    print(f"The local b is {b}")
Not()
print(a) #This Time a = 10 Not excuted 

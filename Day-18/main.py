#Introduction to OOPs
#For Example 
#RAILWAY FORM-------> CLASS(Blueprint)
#OBJECTS(Entity) 
# Harry-----> Information of harry
# Tom -------> Information of tom
# Shubham -----> Information of Shubham
#How To create a class.
class Person:
    name = "Rajat"
    occupation = "Software Developer"
    networth = 2500000
    def info(self):
        print(f"{self.name} is a {self.occupation}")
a = Person()
# print(a.name , a.occupation) #Rajat Software developer
# a.name = "Ritika"
# print(a.name , a.occupation) #We Also Chnage the name and any other info
a.info()
#Self Parameter---> The self Parameter is a refernce to the current instance of the class, and is used to access variables that belongs to the class. 
b = Person()
b.name = "Shaurya"
b.occupation = "Junior Engineer"
b.info()
#Construcators---> It is a special type of method that is automatically called when a new object of a class is created.
class Persons:
     def __init__(self,n,o): #Constructor
         print("Hey I Am a Person.")
         self.name = n
         self.occupation = o

     def info(self):
         print(f"{self.name} is a {self.occupation}")

a = Persons("Harry","Developer")  #Hey I am a person(excuted)
b = Persons("Divya", "HR")         #Hey i am a person(excuted)
a.info()
b.info()
#Decorators----> Simply it decorate the another function or class without changing its original source code.(In simple language it decorate the function)
def greet(fx):
    def mfx():  #Modify fx
        print("Good Morning")
        fx()
        print("Thanks for using this function")
    return mfx
    
@greet
def hello():
    print("Hello World")

hello()
#When arguments in a function:
def greet(fx):
    def mfx(*args , **kwargs):  
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return mfx
@greet
def add(a,b):
    print(a + b)
add(2,3)

# greet(add)(4,5)  


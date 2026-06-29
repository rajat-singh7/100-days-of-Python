# Operator Overloading:
class Vector:
    def __init__(self , i , j ,k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j  + {self.k}k"
    def __add__(self,x):
        return Vector(self.i + x.i, + self.j + x.j ,  + self.k + x.k)

v1 = Vector(3,5,6)
print(v1)

v2 = Vector(1,2,3)
print(v2)

print(v1 + v2)  #For This we need to define __add__:
# print(type(v1 + v2)) # String After chnaging in add function

print(type(v1 + v2))

#Single Inheritance
class Animal:
    def __init__(self,name , species):
        self.name = name 
        self.species = species
    def make_sound(self):
        print("Sound Made By Animal")

class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species = "Dog")
        self.breed = breed
    def make_sound(self):
        print("Bark!")

d = Dog("Dog","Doggerman")
d.make_sound() #bark!

a = Animal("Dog", "Doggerman")
a.make_sound() #sound Made by Animal

#Quick Quiz:
#Implement a cat class by using the anumal class . Add some methods specific to cat.
class Cat(Animal):
    def __init__(self,name,breed,age,colour):
        Animal.__init__(self,name,species= "Cat" )
        self.age = age
        self.colour = colour

    def make_sound(self):
        print("Meow!")
    def Colour(self):
        print("Black")
    def Age(self):
        print(10)

c = Cat("Cat","Catter","Red",7)
c.Age()
c.Colour()
c.make_sound()

# Multiple Inheritance

class Employee:
    def __init__(self,name):
        self.name =  name
    def show(self):
        print(f"The Name is {self.name}")

class Dancer:
    def __init__(self,dance):
        self.dance =  dance

    def show(self):
        print(f"The Dance is {self.dance}")


class DancerEmployee(Dancer,Employee):
    def __init__(self,dance,name):
        self.dance = dance 
        self.name = name


o = DancerEmployee("Kathak","Ruchi")
print(o.name)
print(o.dance)
o.show()
print(DancerEmployee.mro())

# Example demonstrating multiple inheritance and MRO

class Father:
    def skills(self):
        print("Father: Gardening, Programming")

class Mother:
    def skills(self):
        print("Mother: Cooking, Painting")

class Child(Mother, Father): # Follows MRO
    def skills(self):
        print("Child: Dancing")
        # Call parent methods using super()
        super().skills()  
c = Child()
c.skills()

# Show Method Resolution Order 
print("MRO:", Child.mro())








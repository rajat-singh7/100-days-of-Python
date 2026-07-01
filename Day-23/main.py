# Multilevel inheritance:
class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def showDetails(self):
        print(f"Name:{self.name}")
        print(f"Species:{self.species}")
class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species = "Dog")
        self.breed = breed
    def showDetails(self):
        Animal.showDetails(self)
        print(f"Breed:{self.breed}")

class GoldenRetriever(Dog):
    def __init__(self,name,colour):
        Dog.__init__(self,name,breed = "Golden Retriever")
        self.colour = colour

    def showDetails(self):
       Dog.showDetails(self)
       print(f"Colour:{self.colour}")

o = GoldenRetriever("Tommy", "Golden")
o.showDetails()

# Hybrid Inheritance(Like CEO)
class BaseClass:
    pass
class Derived1(BaseClass): #Single Inheritance
    pass
class Derived2(BaseClass):
    pass
class Derived3(Derived1,Derived2): #Multiple Inheritance
    pass

# Hierarchical Inheritance
class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

class Square(Shape):
    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length

    def area(self):
        return self.side_length**2

circle = Circle("Red",7)
square = Square("Yellow",3)
print(circle.area()) 
print(square.area())
# program:
# Shoutouts to everyone:
# Write a program to pronounce list of names using win32 API. If you are given a list l as follows:
# l = ["Ram","Shyam","Rajat", "Dhoni"]
import win32com.client as wincom
# Initialize the speaker
speak = wincom.Dispatch("SAPI.spVoice")
list_of_names = ["Ram","Shyam","Rajat", "Dhoni"]
for name in list_of_names:
    print(f"Shoutout to {name}!")
    speak.Speak(f"Shoutout to {name}") 

# Time Module
# time.time() Function
import time
start_time = time.time()
# Code block whose execution time is to be measured
for i in range(1000):
   print(i)
   i = i + 1
end_time = time.time()
elapsed_time = end_time - start_time
print("Elapsed Time:", elapsed_time, "seconds")

# time.sleep()
print(5)
time.sleep(3)
print("This Is printed after 3 seconds..")


# time.strftime()
t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S",t)
print(formatted_time)


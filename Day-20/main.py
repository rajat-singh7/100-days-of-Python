#  Class Method
class Employee:
    company  = "Apple"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")

    @classmethod   #Modifies the class variable
    def changeCompany(cls,newCompany):
        cls.company = newCompany

e1 = Employee()
e1.name = "Rajat"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.company)
 
# Class Method as Alternative Constructor.
class Professor:
   def __init__(self, name, id, age):
       self.name = name
       self.id = id
       self.age = age
   @classmethod
   def from_string(cls, details):
       name, id, age = details.split(',')
       return cls(name.strip(), id.strip(), int(age))
prof = Professor.from_string("Jack Robins, 2233394, 45")
print(prof.name, prof.id, prof.age)

#dir(), __dict__ , help() Method:
# 1.dir()
x = [1,2,3]
print(dir(x))
print(x.__add__)
print(x.append)
# 2.__dict__
class Person:
    def __init__(self,name,age ):
        self.name = name
        self.age = age
        self.version = 1

p = Person("John", 30)
print(p.__dict__)
# 3.help()
print(help(Person)) 

#Super Keyword  

class ParentClass:
    def parent_method(self):
        print("This is the parent method 1.")

class ChildClass(ParentClass):
    def parent_method(self):
        print("Harry2")
        super().parent_method()
    def child_method(self):
        print("This Is the Child Method.2")
        super().parent_method() #First child class's parent method class

child_object = ChildClass()
child_object.child_method()
child_object.parent_method()

class Employees:
    def __init__(self,name,id):
        self.name = name 
        self.id = id

class Programmer(Employees):
    def __init__(self,name,id, language):
        super. __init__(name,id) #Inheritance Code from Employees Class
        self.language = language

rohan = Employees("Rohan Das", "345")
harry = Employees("Harry 367","Python")
print(harry.name)
print(harry.id)
print(harry.language)

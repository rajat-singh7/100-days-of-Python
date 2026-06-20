#Getters And Setters:
class Employee:
    def __init__(self,salary):
        self._salary = salary #Single underscore suggest a protected variable
    # Getter Method
    def get_salary(self):
        return self._salary
    # Setter Method
    def set_salary(self,amount):
        if amount > 0:
            self._salary = amount
        else:
            print("Salary must Be positive")

# Usage
emp = Employee(5000)
emp.set_salary(9000)    # Must Call as a Function
print(emp.get_salary())  #9000 
#Inheritance 
class Animal:
    def __init__(self, name,sound):
        self.name = name
        self.sound = sound
    
    def showDetails(self):
        print(f"The Name of Animal is {self.name} and his sound is {self.sound}")

    def speak(self):
        return "Some generic sound"
    

class Dog(Animal):
    def speak(self):
        return "Woof!"
d = Dog("German Shephard","woof")
d.showDetails()
d.speak()
# Access Modifiers
# Public Access Modifier
class Person:
   def __init__(self, name, age):
       self.name = name # Public attribute
       self.age = age # Public attribute
   def display(self):
       print(f"Name: {self.name}, Age: {self.age}")
# Example usage
person = Person("Alice", 30)
print(person.name) # Accessible
person.display() # Accessible


# Protected Acccess Modifiers
class Employee:
   def __init__(self, name, salary):
       self._name = name # Protected attribute
       self._salary = salary # Protected attribute
   def _display_salary(self): # Protected method
       print(f"Salary: {self._salary}")
class Manager(Employee):
   def show_details(self):
       print(f"Name: {self._name}")
       self._display_salary()
# Example usage
manager = Manager("Bob", 50000)
manager.show_details() # Accessible within subclass
print(manager._name) # Accessible but discouraged

# Private Access Modifiers
class BankAccount:
   def __init__(self, account_number, balance):
       self.__account_number = account_number # Private attribute(Double Underscore)
       self.__balance = balance # Private attribute
   def __display_balance(self): # Private method
       print(f"Balance: {self.__balance}")
   def access_private(self):
       self.__display_balance() # Accessible within the class
# Example usage
account = BankAccount("12345", 1000)
account.access_private() # Accessible
# print(account.__balance) # Raises AttributeError
print(account._BankAccount__balance) # Access via name mangling (not recommended)

# Static Methods:
class Math:
    def __init__(self,num):
        self.num = num
    def addtoNum(self,n):
        self.num = self.num + n
    @staticmethod
    def add(a,b): #No Argumnet pass there
        return a + b
a =  Math(5)
print(Math.add(9,9))

# Instance variables Vs class variable
class Employees:
    companyName = "Apple" #Class Variable
    no_of_Employees = 0   #Class Variable
    def __init__(self,name):
        self.name = name  #Instance variable
        self.raise_amount = 0.03 #Instance variable
        Employees.no_of_Employees += 1
    def ShowDetails(self):
        print(f"The Name of the employee is {self.name} and the raise amount in {self.no_of_Employees} sized {self.companyName} is {self.raise_amount}")

emp1 = Employees("Rajat")
#If I want to change raise amount of employee Rajat
emp1.raise_amount = 1.2
#And Also wants to change the company name for employee 1
emp1.companyName = "Microsoft"
emp1.ShowDetails()
Employees.companyName = "Google"
print(Employees.companyName)
emp2 = Employees("Rohan")
emp2.ShowDetails()

# Magic/ Dunder Methods In Python
class Employee:
    def __init__(self,name): #Constructor 
        self.name = name
  
    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
            return i
        

e = Employee("Harry")
print(e.name)
print(len(e)) 


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __eq__(self, other):
        return isinstance(other, Vector) and self.x == other.x and self.y == other.y

v1 = Vector(2, 3)
v2 = Vector(4, 5)
print(v1 + v2)   # Vector(6, 8)
print(v1 == v2)  # False
print(repr(v1))  # Vector(2, 3)

# Method Overriding
class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def area(self):
        return self.x * self.y
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
rec = Shape(4,5) 
print(rec.area())
cir = Circle(10)
print(cir.area())


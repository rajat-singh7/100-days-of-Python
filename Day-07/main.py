#Practice Questions on function..
#Define a function print_triangle that print an specific pattern:
#*
#**
#***
#****
#*****
def print_triangle():
    for row in range(1,6):
        print("*" * row)

print_triangle()
#Create a function is_leap_year that takes no parametres and asks the user to input any year, The function should then determine whether the entered year is a leap year and print the result:
def  is_leap_year():
    input_year = int(input("Enter Any year:"))
    if(input_year % 4 == 0):
        if(input_year % 100 == 0):
            if(input_year % 400 == 0):
                print("Input Year is a leap year")
            else:
                print("Input Year is not a leap year")
    else: 
        print("Input Year is not a leap year")
is_leap_year()
#Create a function is even or not:
def Is_even():
    num = int(input("Enter A number:"))
    if(num % 2 == 0):
        print("Number is Even")
    else:
        print("Number is Not Even")
Is_even()
def Is_Palindrome():
    word = input("Enter any word: ")
    if(word == word[::-1]):
        print("Word Is Palindrome")
    else:
        print("Word Is Not a Palindrome")
    
Is_Palindrome() 
#Maximum of three number 
def Max_number(a,b,c):
    if(a > b and a > c):
        print("First number Is Greatest")
    elif(b > c):
        print("Second number is greatest")
    else:
        print("Third number Is greatest")

Max_number(4,7,9)
#Square of any number:
def Square_of_num(number):
    return number ** 2
result = Square_of_num(8)
print(result)
#Sum of two numbers
def Sum(a,b):
    return a + b
result = Sum(4,5)
print(result)
#Write A Function multiply that multiplies two numbers, but can also accept and multiply strings.
def multiply(a , b):
    return a * b
result = multiply("R",5)
print(result)
#Create a function that returns both the area and circumference of a circle given its radius..
import math

def circle_stats(radius):
    area = math.pi * radius **2
    circumference = 2 * math.pi * radius
    return round(area,2), round(circumference,3)
a , c = circle_stats(4)
print("Area:", a , "Circumference:",c) 

#Lambda functions
cube = lambda x : x**3
print(cube(4))
#Lists 
l = [3,6,8,5]
print(type(l))
print(l)
v = ["akash", 34,5.6]
print(v)
print(len(l))
if 3 in l:
    print("Yes")
else:
    print("NO")
if "sh" in "akash":
    print("YES")
else:
    print("NO")
list = [i for i in range(1,9)]
print(list)
#List Methods
(l.append(12))
print(l)
l.sort()
print(l)
l.reverse()
print(l)
l.index(6)
print(l)
l.count(3)
print(l)
#List is Mutable
l[1] = 23
print(l)
#And many more..
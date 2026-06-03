#conditional statements..
a = int(input("Enter your Age:"))
if(a >= 18):
    print("You can drive")
else:
    print("You cannot drive")
apple_price = 220
budget = 200
if(apple_price <= budget):
    print("Alexa , add 1 kg Apples to the cart")
else:
    print("Alexa,do not add Apples to the cart")
number = int(input("Enter the value of num:"))
if(number < 0):
    print("Number is negative")
elif(number == 0):
    print("Number is zero")
else:
    print("Number is positive")
#Nested if statements:
num = 25
if(num < 0):
    print("Number is negative")
elif(num > 0):
    if(num <= 10):
        print("Number is between 1-10")
    elif(num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is equal to zero")

marks = int(input("Enter a no."))
if(marks >= 90):
    print("Grade-A")
elif(marks >= 80 and marks < 90):
    print("Grade-B")
elif(marks >= 70 and marks < 80):
    print("Grade-C")
else:
    print("Grade-D")

value = 6
remainder = 0
if(remainder == value % 2):
    print("Number is even")
else:
    print("Number is odd")

a = 20
b = 25
c = 30
if(a > b and a > c):
    print("A is greatest")
elif(b > c):
    print("B is greatest")
else:
    print("C is greatest")
ram = 155
shyam = 167
krishna = 177
if(ram > shyam and ram > krishna):
    print("Ram is taller both of them")
elif(shyam > krishna):
    print("Shyam is tallest one")
else:
    print("Krishna is one of the tallest boy")

  
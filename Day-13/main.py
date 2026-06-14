#Else with loop:
#For Loop
for i in range(5):
    print(i)
else:
    print("Sorry no i")#Here Else in loop..


for i in range(6):
    print(i)
    if i == 4:
        break

else:
    print("Sorry No i")
#While Loop
i = 0
while i<7:
    print(i)
    i = i + 1
    if i == 4:
        break

else:
     print("Sorry no i ")
#Error Handling in Python
a = input("Enter the number:")
print(f"Multiplication table of {a} is: ")
try:
    for i in range(1,11):
        print(f"{a} x {i} = {int(a)*i}")
except:
    print("Invalid Input!")

print("End Of Program")
#Example No.2
try:
    num = int(input("Enter An Integer: "))
    a = [3,4,5,8]
    print(a[num])
except ValueError:
    print("Number Entered is Not an integer")
except IndexError:
    print("Index error")
#Finally Clause:Most Important Question
def function():
    try:
        l = [1,4,6,3]
        i = int(input("Enter The Index: "))
        print(l[i])
        return 1
    except:
        print("Some Error Occured")
        return 0
    finally:
        print("I Am Always executed ")

x = function()
print(x)
#Raising Custom Errors:(Used to giving error)
b = int(input("enter A number between 5 and 9: "))
if(b<5 or b>9):
    raise ValueError("Value should be between 5 and 9")

#Break and continue statements
name = "Harry"
for i in name:
    print(i)
    if(i == "a"):
        break

for i in range(1,12):
    if(i == 10):
        continue
    print(i)

#Emulate "Do while loop"
a = 50
while True:
    print(a)
    a = a + 1
    if(a % 100 == 0):
        break
for i in range(1,6):
    if i == 3:
        break
    print(i,end = " ")
 
#Function 
def calculate_sum(a,b):
    sum = a + b
    print(sum)

calculate_sum(6,7)
calculate_sum(9,34)
def IsGreater(a,b):
    if(a > b):
        print("First No is Greater")
    else:
        print("Second No is greater")
IsGreater(9,8)
IsGreater(3,7)
#Function Arguments 
#Default argument
def Average(a = 24, b  = 24):
    print("The average of two number:",(a + b)/2)
    return
Average() 
#Required Argumnets
def average(a , b ,c = 5):
    print("The Average of  three numbers is:", (a + b + c)/3)
average(5,5)#C Is optional 
 

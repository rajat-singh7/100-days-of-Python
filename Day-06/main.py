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
 



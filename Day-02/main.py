a = "2"
b = "5"
print(a + b)
#Time to learn typecasting
c = int("5")
d = int("5")
print(c + d)
print(c * d)
print(c / d)
print(c ** d) 
#Trying some thing new
a = 2
b = a + 3
c = a * b
print(a + b + c)#17
#Strings
Sen1 = 'He said, "I Want to eat apple.'
print(Sen1)
sen2 = "He said,\"I want to eat apple."
print(sen2)
#Example of multiline string..
sen3 = '''He said,
Hi Rajat 
hey I am good
"I want to eat apple.'''
print(sen3) 
#Indexing
h = "harry"
print(h[0])
print(h[2])
#print(h[5]) #Throws an error
print(Sen1[3])
print(sen2[3])
#Touching the concept of for loop...
for char in h:
    print(char)

for i in sen3:
    print(i)
#slicing
name = "Raghunath"
print(name[1:4])
print(name[:4])#[0:4]
print(len(name))
print(name[0:])#[0:len(str)]
print(name[-5:-2])
#string methods
print(name.upper())
print(name.lower())
print(name.endswith("th"))
print(name.capitalize())
print(name.find("g"))#tell about index..
print(name.replace("a","u"))
print(sen3.count("I"))
print(sen3.split(" "))#It makes a list...

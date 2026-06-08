#Learning Tuples
tup = (5,6,7,8,66,3)
print(type(tup))
print(tup)
print(tup[2])
print(len(tup))
#Tuples are immutable:
#tuples methods
countries = ("Russia","America","Canada","Singapore","India","Nepal")
print(countries.count("Russia"))
print(countries)
#print(countries.append("Sri Lanka"))#Error We can not append in tuple directly but here a method to append in tuple,First convert tuples in list then do changes and again converts into tuple..
temp = list(countries)
temp.append("Sri Lanka")
countries = tuple(temp)
print(countries)
print(countries.index("India"))#Give index on which element is exists
#Merging of two tuplesL:
east = ("Arunachal Pradesh","Assam","West Bengal","Mizoram","Nagaland","Tripura","Meghalya")
west = ("Rajasthan","Gujarat","Punjab",'Goa',"Maharashtra")
india = east + west
print(india)
#Some Advance level questions:
#Remove duplicates from a list without changing their order:
nums = [2,5,8,4,3,2,2,5,8,4,5,4,1]
unique = []
for i in nums:
    if i not in unique:
        unique.append(i)
print(unique)
#Squares of numbers from 1-10
squares = [i**2 for i in range(1,11)]
print(squares)
#Filters Even numbers:
numbers = [2,4,6,7,2,58,9,3,7,19,34,72]
even = [i for i in numbers if i % 2 ==0]
print(even) 
#Nested acccess 
matrix = [[1,2],[3,6],[7,9]]
print(matrix[1][1])#It Find 6
#Swap without 3rd variable
a = 20
b = 30
a,b = b , a #Firstly make right side tuple b, a then unpack into a ,b 
print(a,b)
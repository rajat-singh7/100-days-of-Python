#Set
s = {1,4,6,8,3,9,4,6,1,3,3,3}
print(type(s))
print(s) 
#Set can store different data types
info = {"Harry",22,True, 4.5,("Rampur")}
print(info)
#How to create an empty set...
python = set()#Use Parenthesis
print(type(python))
#To access set items
for values in info:
    print(values)

#Set Methods
s1 = {2,4,6,8,3,2,9,12,56,78,45}
s2 = {3,6,8,2,4,8,0,65,45,89}
print(s1.union(s2))
print(s1.intersection(s2))
#s1.intersection_update(s2)
print(s1)
print(s1.symmetric_difference(s2))#It prints the values which is not common in both the sets.
print(s1.difference(s2))#s1 - s2
#Disjoint set - The sets in which no elements is commnon..
cities = {"Delhi","Mumbai","Banaras","Kolkata"}
cities2 = {"Kashi","Chennai","Hyderabad","Bangalore"}
print(cities.isdisjoint(cities2))#True
print(cities.issuperset(cities2))#False
print(cities.issubset(cities2))#False
#Adding any other elemnets in any set
cities.add("Begusarai")
print(cities)
cities.remove("Delhi")
print(cities)
#cities.remove("Howrah")#It gives error
#print(cities)
print(cities.pop())#It removes any element from set
info = {"Harry",22,True, 4.5,("Rampur")}
if "Harry" in info:
    print("Harry is present")
else:
    print("Harry is absent")

#Dictionary
dic = {
    "name" :"Rajat Singh",
    "Father_name" : "Jitendra kumar singh",
    "course" : "B.Tech CSE",
    "college_name" : "Maharishi University of information technology",
    "cgpa" : "9.8(upto 6th semester)"
}
print(dic)
print(type(dic))
print(dic["college_name"])#Maharishi university of information technology
print(dic.get("college"))#Similar as above
dic = {
    "name" :"Rajat Singh",
    "Father_name" : "Jitendra kumar singh",
    "course" : "B.Tech CSE",
    "college_name" : "Maharishi University of information technology",
    "cgpa" : "9.8(upto 6th semester)"
}
for keys in dic: #It give us key in our dictionary
    print(keys)
for keys in dic.keys(): #It give us values in our dictionary
    print(dic[keys])
print(dic.items())
#Dictionary Methods
employes_id = {122:45, 145:56,167:78}
employes_id2 = {134:67,456:78,567:89}
employes_id.update(employes_id2)
print(employes_id)
employes_id.pop(122)
print(employes_id)
# del employes_id
# print(employes_id)
# Basic Questions
#Frequency counter
list = ["Apple","Banana","Apple","Banana","Orange","Apple","Orange"]
print(list.count("Apple"))
print(list.count("Orange"))
print(list.count("Banana"))
#Remove multiple elements from a list
mylist = ["Tennis","Hockey","Cricket","Archery","Football"]
del mylist[1:4]
print(mylist)
#Find Any specific element in list
mylist = ["Tennis","Hockey","Cricket","Archery","Football"]
if "Tennis" in mylist:
    print("Found")
#Get the maximum and minimum from a list
list1 = [2,6,7,4,6,8,2,9,0]
print(max(list1))
print(min(list1))
#Make a copy of any list:
list1 = [2,6,7,4,6,8,2,9,0]
list2 = list1.copy()
print(list2)
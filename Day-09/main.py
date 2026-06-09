#Learning About f string
#String Formatting
letter = "Hey My Name is {} and I am from {}"
country = "India"
name = "Rajat"
print(letter.format(name,country))#This Method is used in old programs
#In Modern world use f string
print(f"Hey My name is {name} and I am from {country}")
price = 49.454567
txt = F"For Only {price: .2f}"#.2f mean it show only two digits after decimal
print(txt)
print(f"{2 * 50}")#100
print(type(f"{2 * 14}"))#String

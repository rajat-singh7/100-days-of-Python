# Walrus Operator ---->README.md
a = True
print(a := False) #false
numbers = [1,2,3,4,5]

while (n := len(numbers)) > 0:
    print(numbers.pop())
print(numbers) # Now it will become an empty list...

# foods = list()
# while True:
#     food = input("What Food Do you Like?: ")
#     if food == "quit":
#         break
#     foods.append(food)

# print(foods)

# Now Using Walrus Operator:
foods = list()
while (food := input("What food Do you Like?:")) != "quit":
    foods.append(food)
print(foods)

while (name := input("Enter name (or 'quit'): ")) != "quit":
    print(f"Hello, {name}")

 
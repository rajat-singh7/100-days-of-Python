# Generators in Python
# Example No.01
def generate_numbers(max_value):
   num = 1
   while num <= max_value:
       yield num
       num += 1
# Using the generator
for value in generate_numbers(5):
   print(value)

# Example No.02
# Generator expression to calculate squares
squares = (x * x for x in range(1, 6))
for square in squares:
   print(square)

# Example No.03
def my_generator(n):

    # initialize counter
    value = 0

    # loop until counter is less than n
    while value < n:

        # produce the current value of the counter
        yield value

        # increment the counter
        value += 1

# iterate over the generator object produced by my_generator
for value in my_generator(3):

    # print each value produced by generator
    print(value)

# Example No.04
def PowTwoGen(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1


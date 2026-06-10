#Docstring
def square(n):
    '''Takes in a number n, returns the square of n '''  ##Docstring
    print(n ** 2)

square(5)
print(square.__doc__)#Used to print our docstring
#PEP 8(Python Enhancement Proposal)
#The Primary focus of PEP 8 is to improve the readability and consistency of Python code
#Recursion -- It is a process when a function call to itself..
def factorial(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n - 1)#Here We again call function factorial

print(factorial(3))
print(factorial(4))
print(factorial(5))
 

 #Recursion Example and questions
def factorial(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(6))
#Fibonacci series
def fibonacci_series(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return fibonacci_series(n-1) + fibonacci_series(n-2)
print(fibonacci_series(7)) 
#Find sum of n number
def find_sum(n):
    if(n == 1):
        return 1
    else:
         return n + find_sum(n-1)
print(find_sum(10))
def print_n(n):
    if n == 0:
        return 
    print_n(n - 1)
    print(n , end = " ")

print_n(10)
#String Reverse
def reverse(s):
    if len(s) <= 1:
        return s
    else:
        return s[-1] + reverse(s[:-1])
    
print(reverse("Hello"))
def rev(s):
    if len(s) <= 1:
        return s
    else:
        return s[-1] + reverse(s[:-1])
    
print(rev("My name is Rajat Singh"))
#Palindrome check
def Is_palindrome(a):
    if len(a) <= 1:
        return True
    if a[0] == a[-1]:
        return Is_palindrome(a[1:-1])
    return False

print(Is_palindrome("MADAM"))
 
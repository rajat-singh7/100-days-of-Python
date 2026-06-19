#Today-18|June|2026
#Problem No.01
#Print 123...n without using string methods.
n = int(input("Enter A Number: "))
for i in range(1,n + 1):
    print(i, end="")
#Done

#Problem No.02
# +1 for A and -1 for B then calculate final happiness.
import sys
sys.stdin = open(r"C:\\Users\\ishaw\\OneDrive\\Documents\\GitHub\\100-days-of-Python\Day-18\input.txt")
n,m = map(int,input().split())
array = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

happiness = 0
for num in array:
    if num in A:
        happiness  += 1
    elif num in B:
        happiness -=1
print()
print(happiness)
#
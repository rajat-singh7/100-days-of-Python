#Today-18|June|2026
#Problem No.01
#List Comprehension:
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    result = []
    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                if i+j+k != n:
                    result.append([i,j,k])
  
  
print(result)                  
#Problem No.02
#Find The runner-up
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(set(arr)) #Convert set because of remove repetation then convert it into list
    arr.sort()
    print(arr[-2])

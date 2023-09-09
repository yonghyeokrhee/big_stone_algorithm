n = int(input())

A = list(map(int, input().split()))

sum = 0
maxSum = -int(1e9)

for i in range(n):
    
    sum += A[i]
    maxSum = max(maxSum, sum)
    
    if sum < 0:
        sum = 0
        
print(maxSum)

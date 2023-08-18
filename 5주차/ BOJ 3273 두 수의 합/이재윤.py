N = int(input())

A = list(map(int, input().split()))

target = int(input())

A.sort()

left = 0 
right = len(A)-1
ans = 0 

while left<right:
    
    sum = A[left] + A[right]
    
    if sum < target:
        left += 1 
    elif sum > target:
        right -= 1 
    else:
        ans += 1 
        left += 1 
        right -= 1 
    
print(ans)

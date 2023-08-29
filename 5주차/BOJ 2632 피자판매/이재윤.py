
target = int(input())

m, n = map(int, input().split())

A = []
B = []

for i in range(m):
    num = int(input())
    A.append(num)
    
for i in range(n):
    num = int(input())
    B.append(num)
    
    
    
    
sumA = [0]*2000010
sumB = [0]*2000010

for i in range(m):
    sum = 0
    pos = i
    
    while True:
        
        if pos == i-1:
            break
        
        sum += A[pos]
        sumA[sum] += 1
        pos += 1 
        
        if pos == m:
            if i == 0:
                break
            else:
                pos = 0 
                
                
for i in range(n):
    sum = 0
    pos = i
    
    while True:
        
        if pos == i-1:
            break
        
        sum += B[pos]
        sumB[sum] += 1
        pos += 1 
        
        if pos == n:
            if i == 0:
                break
            else:
                pos = 0 
                
          
ans = 0           
ans += sumA[target]
ans += sumB[target]


for i in range(1, target):
    
    cnt1 = sumA[i]
    cnt2 = sumB[target-i]

    ans += (cnt1*cnt2)
    
    
print(ans)


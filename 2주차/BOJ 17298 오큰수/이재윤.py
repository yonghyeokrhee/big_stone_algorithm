N = int(input())

A = list(map(int, input().split()))
ans = [-1]*N
stk = []

for i in range(N):
    
    curr = A[i]
    
    while stk:
        num, pos = stk[len(stk)-1][0], stk[len(stk)-1][1]
        
        if num < curr:
            stk.pop(len(stk)-1)
            ans[pos] = curr
        else:
            break 
        
    
    if i == N-1:
        break
    
    
    stk.append((curr, i))
    
    
for i in range(N):
    print(ans[i],end=' ')
        
        
        
        
        
        
        
    

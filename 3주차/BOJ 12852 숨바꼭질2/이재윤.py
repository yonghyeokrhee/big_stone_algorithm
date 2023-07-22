from collections import deque

N, K = map(int, input().split())
count = [0]*100010
minTime = int(1e9) 
ans = 0 

def bfs(start):
    
    global minTime
    global ans
    
    q = deque()
    q.append(start)
    count[start] = 1
    
    while q:
        x = q.popleft()
        
        if x == K:
            // 이렇게 판단하는 것이 매우 중요하다 
            if minTime == int(1e9) or (minTime == count[x]-1):
                minTime = count[x]-1
                ans += 1 
            
        for i in range(3):
            nx = 0
            
            if i == 0:
                nx = x-1
            elif i == 1:
                nx = x+1
            else:
                nx = 2*x 
            
            // 이렇게 판단하는 것이 매우 중요하다
            // 어느 케이스에 가능한지 판단해야 한다 
            if 0<=nx and nx<=100000 and (count[nx] == 0 or (count[nx] == count[x] + 1)):
                count[nx] = count[x] + 1 
                q.append(nx)
            
            
            
            
    
    


bfs(N)


print(minTime)
print(ans)

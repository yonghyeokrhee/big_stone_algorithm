from collections import deque

N, K = map(int, input().split())
count = [0]*100010
parent = [-1]*100010
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
            if minTime == int(1e9):
                minTime = count[x]-1
                break
            
        for i in range(3):
            nx = 0
            
            if i == 0:
                nx = x-1
            elif i == 1:
                nx = x+1
            else:
                nx = 2*x 
            
            // parent라는 배열을 활용한다는 아이디어가 중요하다 
            if 0<=nx and nx<=100000 and count[nx] == 0:
                count[nx] = count[x] + 1 
                parent[nx] = x 
                q.append(nx)
            
                        
bfs(N)

print(minTime)
arr = []
arr.append(K)

while True:
    
    if parent[K] == -1:
        break 
    
    arr.append(parent[K])
    K = parent[K]
    
for i in range(len(arr)-1, -1, -1):
    print(arr[i], end=' ')






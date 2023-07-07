// N과 M 그리고 입력값들을 잘 배열하는 것이 중요하다 

import sys
sys.setrecursionlimit(10**6)

M, N, K = map(int, input().split())

visited = [[False]*N for _ in range(M)]
area = 0 
cnt = 0 
arr = []  
 
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y, visited):
     
    global cnt 
    cnt += 1 
    visited[x][y] = True 
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<=nx and nx < M and 0<=ny and ny < N and visited[nx][ny] == False:
            dfs(nx, ny, visited)
    
    

for i in range(K):
    
    y1, x1, y2, x2 = map(int, input().split())
    
    for i in range(x1, x2):
        for j in range(y1, y2):
            visited[i][j] = True 
    

for i in range(M):
    for j in range(N):
        if visited[i][j] == False:
            area += 1 
            cnt = 0 
            dfs(i, j, visited)
            arr.append(cnt) 
            

arr.sort() 
print(area)
for num in arr:
    print(num, end=' ')


    
    

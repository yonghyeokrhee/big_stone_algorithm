// 비가 내리는 높이가 0일 때를 고려해야 한다 
// 파이썬에서 재귀를 사용할 때는 setrecursionlimit을 해줘야 한다 

import sys 
sys.setrecursionlimit(10 ** 6)

N = int(input())

board = [] 
maxHeight = 0
maxArea = 0 
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y, visited):
    
    visited[x][y] = True 
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<=nx and nx < N and 0<=ny and ny < N and visited[nx][ny] == False:
            dfs(nx, ny, visited)
    
    

for i in range(N):
    tmp = list(map(int, input().split()))
    board.append(tmp)
    
for i in range(N):
    for j in range(N):
        maxHeight= max(maxHeight, board[i][j])
    
for i in range(0, maxHeight):
    visited = [[False]*N for _ in range(N)]
    area = 0 
    
    for j in range(N):
        for k in range(N):
            if board[j][k] <= i:
                visited[j][k] = True 
    
    for j in range(N):
        for k in range(N):
            if visited[j][k] == False: 
                area += 1 
                dfs(j, k, visited)
    
    maxArea = max(maxArea, area) 

print(maxArea)
    
    
    
    

// pypy3로 돌리니까 시간 초과가 나지 않았다 

from collections import deque

H, W = map(int, input().split())

board = []
totalMaxDistance = -int(1e9)
visited = [[False]*W for _ in range(H)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(board, sx, sy):
    
    global totalMaxDistance
    
    check = [[0]*W for _ in range(H)]

    pq = []
    q = deque()
    q.append((sx, sy))
    check[sx][sy] = 1 
    cnt = 1
    maxDistance = -int(1e9)
    
    while q: 
        
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx and nx<H and 0<=ny and ny<W and check[nx][ny] == 0 and board[nx][ny] == 'L':
                check[nx][ny] = check[x][y] + 1 
                cnt = max(cnt, check[nx][ny])
                q.append((nx, ny))
                
    
    maxDistance = cnt
    totalMaxDistance = max(totalMaxDistance, maxDistance)            
        
        
    
  
for i in range(H):
    
    row = input()
    tmp = [] 
    
    for j in range(0,W):
        tmp.append(row[j])
    board.append(tmp)
    
lands = []
    
for i in range(H):
    for j in range(W):
        if board[i][j] == 'L':
            lands.append((i,j))
            
for i in range(0, len(lands)):
    bfs(board, lands[i][0], lands[i][1])
    
print(totalMaxDistance-1)  
    

R, C, K = map(int, input().split())

board = [] 
visited = [[False]*(C) for _ in range(R)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
ans = 0 

for i in range(R):
    row = input()
    tmp = [] 
    
    for j in range(C):
        tmp.append(row[j])
    
    board.append(tmp)
    
    
def dfs(x, y, dist):
    
    global ans
    
    if x == 0 and y == C-1:
        if dist == K:
            ans += 1 
            
        return 
    
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        
        if 0<=nx and nx<R and 0<=ny and ny<C and board[nx][ny] == '.' and visited[nx][ny] == False:
                visited[nx][ny] = True
                dfs(nx, ny, dist+1)
                visited[nx][ny] = False 
                
                
    
    

visited[R-1][0] = True
dfs(R-1, 0, 1)    
    
    
print(ans)
    

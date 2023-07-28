R, C = map(int, input().split())

board = [] 
visited = [[False]*(C) for _ in range(R)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
maxlen = -int(1e9)

for i in range(R):
    sentence = input()
    tmp = [] 
    
    for j in range(C):
        tmp.append(sentence[j])
    
    board.append(tmp)
    
    
def dfs(x, y, ans):
    
    global maxlen
    
    maxlen = max(maxlen, len(ans))
    
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        
        if 0<=nx and nx<R and 0<=ny and ny<C and visited[nx][ny] == False:
            if board[nx][ny] not in ans:
                visited[nx][ny] = True
                ans += board[nx][ny]
                dfs(nx, ny, ans)
                ans = ans[:-1]
                visited[nx][ny] = False 
                
                
    
    

ans = board[0][0]
maxlen = 1 

dfs(0, 0, ans)    
    
    
print(maxlen)
    

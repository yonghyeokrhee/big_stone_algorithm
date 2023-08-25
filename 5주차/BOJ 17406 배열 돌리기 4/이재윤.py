// 1시간

N, M, K = map(int, input().split())

board = [] 
cals = [] 
check = [False]*K


minASum = int(1e9)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    
    
for i in range(K):
    row = list(map(int, input().split()))
    cals.append(row)
    
    
def rotate(sx, sy, ex, ey):
    
    tmpBoard = [[0]*M for _ in range(N)]
    dir = 1 
    
    x = sx
    y = sy
    
    
    while True:
        
        nx = x + dx[dir]
        ny = y + dy[dir]
        
        if not (sx<=nx and nx<=ex and sy<=ny and ny<=ey):
            nx -= dx[dir]
            ny -= dy[dir]
            
            if dir == 0:
                dir = 1
            elif dir == 1:
                dir = 2
            elif dir == 2:
                dir = 3
            elif dir == 3:
                dir = 0 
                
            nx += dx[dir]
            ny += dy[dir]
            
            
        tmpBoard[nx][ny] = board[x][y]
        
        x = nx
        y = ny
        
        if x == sx and y == sy:
            break
        
    
    
    for i in range(N):
        for j in range(M):
            if (i == sx and sy <= j and j<=ey) or (i == ex and sy<=j and j<=ey) or (j==sy and sx <= i and i<= ex) or (j == ey and sx <= i and i <= ex):
                board[i][j] = tmpBoard[i][j]

    
    
    
    
def rotates(r, c, s):
    
    
    
    
    while s != 0:
    
        sx = r - s
        sy = c - s
        ex = r + s
        ey = c + s 
        
        rotate(sx, sy, ex, ey)
    
        s -= 1 
    
    
    
    
    
def unrotate(sx, sy, ex, ey):
    
    tmpBoard = [[0]*M for _ in range(N)]
    dir = 2 
    
    x = sx
    y = sy
    
    while True:
        
        nx = x + dx[dir]
        ny = y + dy[dir]
        
        if not (sx<=nx and nx<=ex and sy<=ny and ny<=ey):
            nx -= dx[dir]
            ny -= dy[dir]
            
            if dir == 0:
                dir = 3
            elif dir == 1:
                dir = 0
            elif dir == 2:
                dir = 1
            elif dir == 3:
                dir = 2 
                
            nx += dx[dir]
            ny += dy[dir]
            
            
            
        tmpBoard[nx][ny] = board[x][y]
        
        x = nx
        y = ny
        
        if x == sx and y == sy:
            break
        
    
    
    for i in range(N):
        for j in range(M):
            if (i == sx and sy <= j and j<=ey) or (i == ex and sy<=j and j<=ey) or (j==sy and sx <= i and i<= ex) or (j == ey and sx <= i and i <= ex):
                board[i][j] = tmpBoard[i][j]
    
    

    
    
    
def unrotates(r, c, s):
    
    
    while s != 0:
        
        sx = r - s
        sy = c - s
        ex = r + s
        ey = c + s
        
        unrotate(sx, sy, ex, ey)
        
        s -= 1 
    
    
    
        

def getA():
    
    minRowSum = int(1e9)
    
    for i in range(N):
        rowSum = sum(board[i])
        minRowSum = min(minRowSum, rowSum)
    
    return minRowSum
        
    
    
    
def dfs(cnt):
    
    
    global minASum
    
    if cnt == K:
        res = getA()
        minASum = min(minASum, res)
        
        
        return 
        
        
    for i in range(K):
        if check[i] == False:
            check[i] = True
            rotates(cals[i][0]-1, cals[i][1]-1, cals[i][2])
            dfs(cnt+1)
            check[i] = False
            unrotates(cals[i][0]-1, cals[i][1]-1, cals[i][2])
            

dfs(0)


print(minASum)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


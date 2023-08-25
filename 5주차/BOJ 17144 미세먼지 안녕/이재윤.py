// 1시간 40분

R, C, T = map(int, input().split())

board = [] 
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(R):
    row = list(map(int, input().split()))
    board.append(row)
    
    
time = 0 


def spread(board):
    
    tmpBoard = [[0]*C for _ in range(R)]
    
    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:
                amount = board[i][j]
                cnt = 0 
                
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    
                    if 0<=nx and nx < R and 0<=ny and ny < C and board[nx][ny] != -1:
                        tmpBoard[nx][ny] += amount // 5
                        cnt += 1 
    
                tmpBoard[i][j] += amount - cnt*(amount//5)
                
              
            elif board[i][j] == -1:
                tmpBoard[i][j] = -1
                
    
    for i in range(R):
        for j in range(C):
            board[i][j] = tmpBoard[i][j]
                                
                
    

def airConditionerUpper(sx, sy, ex, ey):
    
    dir = 0 
    
    x = sx
    y = sy 
    
    
    tmpBoard = [[0]*C for _ in range(R)]
    
    
    while True:
        
        nx = 0
        ny = 0 
        
        if dir == 0:
            nx = x + dx[2]
            ny = y + dy[2]
        elif dir == 1:
            nx = x + dx[3]
            ny = y + dy[3]
        elif dir == 2:
            nx = x + dx[0]
            ny = y + dy[0]
        elif dir == 3:
            nx = x + dx[1]
            ny = y + dy[1]
    
        if board[nx][ny] == -1:
            tmpBoard[nx][ny] = -1
        else:
            tmpBoard[nx][ny] = board[x][y]
            
        
        x += dx[dir]
        y += dy[dir]
        
            
        
        if 0<=x and x < ex+1 and 0<=y and y < C:
            if x == ex and y == ey:
                break
            else:
                continue
        else:
            x -= dx[dir]
            y -= dy[dir]
            
            if dir == 0:
                dir = 1
            elif dir == 1:
                dir = 2
            elif dir == 2:
                dir = 3
            elif dir == 3:
                dir = 0 
                
            
            x += dx[dir]
            y += dy[dir]
            
            
    for i in range(R):
        for j in range(C):
            if (i == 0 and 0<= j and j<C) or (i == ex and 0<=j and j<C) or (j == 0 and 0<=i and i<=ex) or (j == C-1 and 0<=i and i<=ex):
                board[i][j] = tmpBoard[i][j]
                
                
                

def airConditionerLower(sx, sy, ex, ey):
    
    dir = 2
    
    x = sx
    y = sy 
    
    
    tmpBoard = [[0]*C for _ in range(R)]
    
    
    
    while True:
        
        nx = 0
        ny = 0 
        
        if dir == 0:
            nx = x + dx[2]
            ny = y + dy[2]
        elif dir == 1:
            nx = x + dx[3]
            ny = y + dy[3]
        elif dir == 2:
            nx = x + dx[0]
            ny = y + dy[0]
        elif dir == 3:
            nx = x + dx[1]
            ny = y + dy[1]
    
        if board[nx][ny] == -1:
            tmpBoard[nx][ny] = -1
        else:
            tmpBoard[nx][ny] = board[x][y]
            
        
        x += dx[dir]
        y += dy[dir]
        
            
        
        if ex<=x and x < R and 0<=y and y < C:
            if x == ex and y == ey:
                break
            else:
                continue
        else:
            x -= dx[dir]
            y -= dy[dir]
            
            if dir == 0:
                dir = 3
            elif dir == 1:
                dir = 0
            elif dir == 2:
                dir = 1
            elif dir == 3:
                dir = 2 
                
            
            x += dx[dir]
            y += dy[dir]
            
            
                
    for i in range(R):
        for j in range(C):
            if (i == ex and 0<= j and j<C) or (i == R-1 and 0<=j and j<C) or (j == 0 and ex<=i and i<=R-1) or (j == C-1 and ex<=i and i<=R-1):
                board[i][j] = tmpBoard[i][j]
    
    
        
aux = 0
auy = 0

alx = 0
aly = 0
cnt = 0     
    



for i in range(R):
    if board[i][0] == -1 and cnt == 0:
        aux = i
        auy = 0
        cnt += 1 
    elif board[i][0] == -1 and cnt == 1:
        alx = i
        aly = 0
        break 


sum = 0 


while True:
    
    if time == T:
        break 
    
    spread(board)
    
    airConditionerUpper(aux-1, 0, aux, 0)
    airConditionerLower(alx+1, 0, alx, 0)
    
    tmpSum = 0 
        
    for i in range(R):
        for j in range(C):
           if board[i][j] != -1:
               tmpSum += board[i][j]
               
    sum = tmpSum
    
    time += 1   


print(sum)

    
    
    
    

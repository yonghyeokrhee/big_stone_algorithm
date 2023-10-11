N, M, K, C = map(int, input().split())

board = [] 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dx2 = [-1, -1, 1, 1]
dy2 = [-1, 1, -1, 1]

for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    
totalKilledTrees = 0 
year = 0 

killerBoard = [[0]*N for _ in range(N)]


def grow():
    
    addTrees = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if board[i][j] > 0:
                
                cnt = 0 
                
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                
                    if 0<=nx and nx<N and 0<=ny and ny<N and board[nx][ny] > 0:
                        cnt += 1 
                
                
                addTrees[i][j] = cnt 
                
    
    
    for i in range(N):
        for j in range(N):
            board[i][j] += addTrees[i][j] 



def breed(): 
    
    
    
    addTrees = [[0]*N for _ in range(N)]
    
    
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0:
                
                cnt = 0 
                
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    
                    if 0<=nx and nx<N and 0<=ny and ny<N and board[nx][ny] == 0 and killerBoard[nx][ny] == 0:
                        cnt += 1 
                        
                
                if cnt > 0:
                    
                    addTree = board[i][j] // cnt 
                    
                    for k in range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        
                        if 0<=nx and nx<N and 0<=ny and ny<N and board[nx][ny] == 0 and killerBoard[nx][ny] == 0:
                            addTrees[nx][ny] += addTree 
                            
    
    for i in range(N):
        for j in range(N):
            board[i][j] += addTrees[i][j] 
            
            
    
    
    
    
    
def findMaximumTreeKill():
    
    killTrees = [] 
    
    for i in range(N):
        for j in range(N):
            
            if board[i][j] > 0:
                killTree = board[i][j] 
                
                
                for k in range(4): 
                    sx = i
                    sy = j 
                    for l in range(K):
                        nx = sx + dx2[k]
                        ny = sy + dy2[k]
                        
                        if 0<=nx and nx<N and 0<=ny and ny<N and board[nx][ny] > 0:
                            killTree += board[nx][ny]
                            sx = nx
                            sy = ny 
                        else:
                            break
                        
                killTrees.append([i, j, killTree])
    

                
                
    killTrees.sort(key=lambda x:[-x[2], x[0], x[1]])
  
    
    if len(killTrees) == 0:
        return None
    else:
        return killTrees[0]            
        
        
        
def checkBoard():
    
    treeCnt = 0 
    
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0:
                treeCnt += 1 
                
                
    if treeCnt == 0:
        return True
        
    
    return False 
    



def spreadKiller(x, y):
    
    board[x][y] = 0 
    killerBoard[x][y] = C 
    
    for k in range(4):
        
        sx = x
        sy = y 
        
        
        for l in range(K):
            nx = sx + dx2[k]
            ny = sy + dy2[k]
            
            if 0<=nx and nx<N and 0<=ny and ny<N and board[nx][ny] > 0:
                board[nx][ny] = 0 
                killerBoard[nx][ny] = C
                sx = nx
                sy = ny 
            elif 0<=nx and nx<N and 0<=ny and ny<N and board[nx][ny] <= 0:
                killerBoard[nx][ny] = C
                break
            else:
                break 
            
              

def decreaseKiller():
    
    
    for i in range(N):
        for j in range(N):
            if killerBoard[i][j] > 0:
                killerBoard[i][j] -= 1 


while True:
    
    if checkBoard() == True:
        break 
    
    grow()
    
    breed() 
    
    killTreeInfo = findMaximumTreeKill()
    
    if killTreeInfo != None:
        x = killTreeInfo[0]
        y = killTreeInfo[1]
        killedTrees = killTreeInfo[2]
        totalKilledTrees += killedTrees 
        decreaseKiller() 
        spreadKiller(x, y)
    else:
        decreaseKiller() 
    
    year += 1 
    
    if year == M:
        break 



print(totalKilledTrees) 

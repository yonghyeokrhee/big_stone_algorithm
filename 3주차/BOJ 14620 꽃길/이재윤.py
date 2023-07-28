N = int(input())

board = [] 
visited = [[False]*(N) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

minSum = int(1e9)


for i in range(N):
    tmp = list(map(int, input().split()))
    board.append(tmp)
    

def getSum(x, y, sign):
    
    tmpSum = 0
    tmpSum += board[x][y]
    visited[x][y] = sign
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        tmpSum += board[nx][ny]
        visited[nx][ny] = sign
        
    return tmpSum 

def dfs(sx, sy, cnt, sum):
    
    global minSum 
    
    if cnt == 3: 
        minSum = min(minSum, sum)
        return 
    
    
    for i in range(N):
        for j in range(N):
            if ((i==sx and j>=sy) or (i>sx)) and visited[i][j] == False:
                
                isSelectable = True 
                
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    
                    if 0<=nx and nx < N and 0<=ny and ny <N and visited[nx][ny] == False:
                        continue
                    else:
                        isSelectable = False 
                        break 
                
                if isSelectable == True:
                    sum += getSum(i, j, True)      
                    dfs(i, j, cnt+1, sum)
                    sum -= getSum(i, j, False)
                        
                        

dfs(0, 0, 0, 0)

print(minSum)








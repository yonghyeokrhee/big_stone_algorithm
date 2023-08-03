
N, L = map(int, input().split())
board = [] 

row = [True]*N
ans = 0 

for i in range(N):
    tmp = list(map(int, input().split()))
    board.append(tmp)
    


def checkRow(board, road):

    global ans     
    
    row = [True]*N
    
    for i in range(N):
        for j in range(N-1):
            if board[i][j+1]-board[i][j] >= 2:
                row[i] = False
                break 
            
            
            if board[i][j+1]-board[i][j] == 1:
                
                tmpJ = j 
                num = board[i][j]
                
                if (tmpJ+1)-L < 0:
                    row[i] = False
                    break
                
                cnt = 0 
                
                while cnt != L:
                    if num == board[i][tmpJ]:
                        road[i][tmpJ] = True 
                        cnt += 1 
                        tmpJ -= 1
                    else:
                        row[i] = False
                        break
    
    for i in range(N):
        if row[i] == False:
            continue 
        
        for j in range(N-1, 0, -1):
            if board[i][j-1]-board[i][j] >= 2:
                row[i] = False
                break 
            
            
            if board[i][j-1]-board[i][j] == 1:
                
                tmpJ = j 
                num = board[i][j]
                
                if tmpJ+L > N:
                    row[i] = False
                    break 
                
                cnt = 0 
                
                while cnt != L:
                    if road[i][tmpJ] == True:
                        row[i] = False
                        break
                    else:
                        if num == board[i][tmpJ]:
                            road[i][tmpJ] = True
                            cnt += 1 
                            tmpJ += 1 
                        else:
                            row[i] = False
                            break 
    
    for val in row:
        if val == True:
            ans += 1 


    
road = [[False]*N for _ in range(N)]



checkRow(board, road)

newBoard = [] 


for j in range(0, N):
    tmp = [] 
    for i in range(0, N):
        tmp.append(board[i][j])
    newBoard.append(tmp)

road = [[False]*N for _ in range(N)]

checkRow(newBoard, road)

print(ans)



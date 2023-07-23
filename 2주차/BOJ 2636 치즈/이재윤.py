from collections import deque

R, C = map(int, input().split())

board = []
air = [[False]*C for _ in range(R)]
visited = [[False]*C for _ in range(R)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(R):
    tmp = list(map(int, input().split()))
    board.append(tmp)
    
    
time = 0 
total = 0
arr = [] 


for i in range(R):
    for j in range(C):
        if board[i][j] == 1:
            total += 1 



def bfs(x, y):
    
    q = deque()
    q.append((x,y))
    air[x][y] = True 
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx and nx <R and 0<=ny and ny < C and board[nx][ny] == 0 and air[nx][ny] == False:
                air[nx][ny] = True 
                q.append((nx,ny))
    
def isMelt(x, y):
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<=nx and nx<R and 0<=ny and ny<C and air[nx][ny] == True:
            return True 
    
    return False 
    

def cheeseBFS(x, y):
    
    global cnt 
    
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    
    
    while q:
        
        x, y = q.popleft()
        res = isMelt(x, y)
        if res == True:
            board[x][y] = 0 
            cnt += 1 
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx and nx<R and 0<=ny and ny<C and board[nx][ny] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append((nx,ny))



def checkAir():
    bfs(0, 0)



def meltCheck():
    
    for i in range(R):
        for j in range(C):
            if board[i][j] == 1 and visited[i][j] == False:
                cheeseBFS(i, j)


while True:
    
    if total == 0:
        break 
    
    cnt = 0 
    
    air = [[False]*C for _ in range(R)]
    visited = [[False]*C for _ in range(R)]
    
    checkAir() 
    
    meltCheck()
    
    arr.append(cnt)
    
    total -= cnt 
    
    time += 1 


print(time)
print(arr[len(arr)-1])










    

import sys
sys.setrecursionlimit(10**6) 

N, M = map(int, input().split())
walls = [[[[False for i in range(60)] for j in range(60)] for k in range(60)] for depth in range(60)]
visited = [[False]*(N+1) for _ in range(M+1)]

dx = [1, 0, -1 , 0]
dy = [0, 1, 0, -1]
cnt = 0 
maxRoom = 0 

def toBinary(num):
    
    ansStr = ""
    
    while num != 0:
        
        remain = num % 2 
        ansStr += str(remain)
        num = num // 2 
        
    if len(ansStr) == 3:
        ansStr = ansStr + '0' 
    elif len(ansStr) == 2:
        ansStr = ansStr + '00'
    elif len(ansStr) == 1:
        ansStr = ansStr + '000'
        
    return ansStr[::-1]

for i in range(1, M+1):
    row = list(map(int, input().split()))
    
    for j in range(1, N+1):
        num = row[j-1] 
        
        ans = toBinary(num)
        
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            
            if ans[k] == '1':
                walls[i][j][nx][ny] = True 
                
                


ans = [] 



def dfs(x, y):
    
    global cnt 
    visited[x][y] = True 
    cnt += 1 
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 1<=nx and nx <= M and 1<=ny and ny <= N and visited[nx][ny] == False and walls[x][y][nx][ny] == False:
            dfs(nx, ny)


for i in range(1, M+1):
    for j in range(1, N+1):
        if visited[i][j] == False:
            cnt = 0 
            dfs(i, j)
            ans.append(cnt)
            
            
print(len(ans))
ans.sort(reverse=True)
print(ans[0])

wallsInfo = [] 


for i in range(1, M+1):
    for j in range(1, N+1):
        for k in range(1, M+1):
            for l in range(1, N+1):
                if walls[i][j][k][l] == True:
                    wallsInfo.append((i,j,k,l))
                
for wall in wallsInfo: 
    walls[wall[0]][wall[1]][wall[2]][wall[3]] = False
    walls[wall[2]][wall[3]][wall[0]][wall[1]] = False
    maxCnt = 0  
    
    for i in range(1, M+1):
        for j in range(1, N+1):
            visited[i][j] = False
    
    for i in range(1, M+1):
        for j in range(1, N+1):
            if visited[i][j] == False:
                cnt = 0 
                dfs(i, j)
                maxCnt = max(maxCnt, cnt)

    maxRoom = max(maxRoom, maxCnt)
    
    walls[wall[0]][wall[1]][wall[2]][wall[3]] = True 
    walls[wall[2]][wall[3]][wall[0]][wall[1]] = True

print(maxRoom)
        
        
        
        

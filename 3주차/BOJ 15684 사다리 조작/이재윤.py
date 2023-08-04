// cnt>= minCnt로 검사해야 한다
// 왜냐하면 minCnt가 현재 있다고 하더라도, 그 값이 최소임을 보장할 수 없기 때문이다. 
// 또한 checkResult에서도 if, elif로 검사를 해야 한다 
// 그리고 if cnt == 3일 때 리턴을 해줘야 한다 

N, M, H = map(int, input().split())

line = [[False]*(N+1) for _ in range(H+1)]

for i in range(M):
    a, b = map(int, input().split())
    line[a][b] = True 
   
minCnt = int(1e9)

def checkResult():
    
    for i in range(1, N+1):
        start = i 
        x, y = 1, i 
        
        while x != H+1:
            if line[x][y] == True:
                y += 1
            elif line[x][y-1] == True:
                y -= 1
            
            x += 1 
        
        if start != y:
            return False
        
    return True 
    
    
def dfs(cnt):
    
    global minCnt
    
    if cnt >= minCnt:
        return  
    
    if checkResult() == True:
        minCnt = min(minCnt, cnt)
        return 
    
    if cnt == 3:
        return 
    
    
    for i in range(1, H+1):
        for j in range(1, N):
            if (line[i][j] == False and line[i][j+1] == False and line[i][j-1] == False):
                line[i][j] = True
                dfs(cnt+1)
                line[i][j] = False 
    
    
dfs(0)
if minCnt == int(1e9):
    print(-1)
else:
    print(minCnt)

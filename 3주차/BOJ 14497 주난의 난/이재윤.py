// 문제의 조건에 유의해야 한다
// BFS+DFS 조합해서 풀면 좋다 

from collections import deque

N, M = map(int, input().split())

x1, y1, x2, y2 = map(int, input().split())

board = [] 
ans = 0 
visited = [[0]*M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    row = input()
    tmp = [] 
    
    for j in range(M):
        if row[j] == '#':
            tmp.append(0)
        elif row[j] == '*':
            tmp.append(-1)
        else:
            tmp.append(int(row[j]))
    
    board.append(tmp)
    
    
def printVisited():
    
    for i in range(N):
        for j in range(M):
            print(visited[i][j], end=' ')
        print('', end='\n')
        
    print('', end='\n')

    
    
def spread(x, y, time):
    
    
    q = deque()
    q.append((x,y))
    global ans 
   
    
    while q:
        x, y = q.popleft()
        
        if x == x2-1 and y == y2-1:
            ans = time
            break 
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx and nx < N and 0<=ny and ny < M:
                
                if board[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = time
                    q.append((nx, ny))
                
                if board[nx][ny] == 1 and visited[nx][ny] == 0:
                    board[nx][ny] = 0
                    visited[nx][ny] = time 
        
   
   


def dfs(time):
    
    global ans
    if time == 0:
        spread(x1-1, y1-1, time+1)
    else:
        for i in range(N):
            for j in range(M):
                if visited[i][j] == time:
                    spread(i, j, time+1)
    
    if ans != 0:
        return 
    
    else:    
        dfs(time+1) 
    
    
    
        
dfs(0)        
        
print(ans)    
        
        
        
        
        
        
        

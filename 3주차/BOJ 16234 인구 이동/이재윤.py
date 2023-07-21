// line을 굳이 배열로 관리할 필요가 없다
// -> 그냥 if문에서 처리해주면, 시간을 많이 절약할 수 있따
// 시간이 그래도 길게 나온다. 리팩터링이 필요할듯하다 
// 이 문제는 bfs로 푸는 것이 좋다.
// bfs로 푸는 것이 좋은지, dfs로 푸는 것이 좋은지에 대한 시각을 길러야 한다 

from collections import deque 

N, L, R = map(int, input().split())

board = []
visited = [[0]*N for _ in range(N)]

sum = 0
cnt = 0 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    tmp = list(map(int, input().split()))
    board.append(tmp)
            
def bfs(x, y, order):
    
    global cnt
    global sum 
    
    q = deque()
    q.append((x,y))
    visited[x][y] = order
    sum += board[x][y]
    cnt += 1 
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx and nx < N and 0<=ny and ny < N and visited[nx][ny] == 0 and L<=abs(board[x][y]-board[nx][ny]) and abs(board[x][y]-board[nx][ny]) <=R :
                visited[nx][ny] = order 
                sum += board[nx][ny]
                cnt += 1 
                q.append((nx,ny))
    
     
        
        
day = 0

while True:
    
    visited = [[0]*N for _ in range(N)]
  
    order = 1 
    populations = [0]*10000

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                sum = 0
                cnt = 0 
                bfs(i, j, order)
                avg = sum // cnt
                populations[order] = avg
                order += 1 
    
    if order == (N*N)+1:
        break
    
    for i in range(N):
        for j in range(N):
            num = visited[i][j]
            board[i][j] = populations[num]

    
    
    day += 1 


print(day)
        
        

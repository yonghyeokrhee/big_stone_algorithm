// 큐를 쓰면 된다
// 불을 먼저 옮기고, 그 다음에 지훈이를 옮겨야 한다
// 왜냐면, 어차피 불이 갈 수 있는 자리는, 지훈이는 가봤자 타기 때문에 없어지기 때문이다
// 큐를 쓰고, 그 큐를 그냥 대입해줘도 된다. 
// 탈출 조건을 잘 잡는 것이 중요하다 
// 나의 부족함을 잘 알아야 한다. 겸손해야 한다. 

from collections import deque

R, C = map(int, input().split())

board = [['0']*C for _ in range(R)] 
jihoon = deque()
fire = deque() 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(R):
    tmp = input()
    
    for j in range(C):
        board[i][j] = tmp[j]
        

for i in range(R):
    for j in range(C):
        if board[i][j] == 'J':
            jihoon.append((i,j))
        
        if board[i][j] == 'F':
            fire.append((i,j))
           
time = 0            
            

while True:

    time += 1 
    
    nextJihoon = deque()
    nextFire = deque()
    out = False
    
    while fire:
        x, y = fire.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
    
            if 0<=nx and nx < R and 0<=ny and ny < C and (board[nx][ny] == '.' or board[nx][ny] == 'J'):
                board[nx][ny] = 'F'
                nextFire.append((nx,ny))
                
    while jihoon:
        x, y = jihoon.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
    
            if nx<=-1 or nx>=R or ny<=-1 or ny>=C:
                out = True 
            
            if 0<=nx and nx < R and 0<=ny and ny < C and board[nx][ny] == '.':
                board[nx][ny] = 'J'
                nextJihoon.append((nx,ny))
                
    if out == True:
        break

    if len(nextJihoon) == 0:
        time = -1
        break 
    
    
    jihoon = nextJihoon
    fire = nextFire 
    

if time == -1:
    print("IMPOSSIBLE")
else:
    print(time)








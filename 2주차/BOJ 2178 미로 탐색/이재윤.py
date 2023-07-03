// BFS를 써서 풀면 되는 문제이다
// 큐에 추가할 때는 append, 왼쪽에서 제거할 때는 popleft를 활용한다 

from collections import deque

N, M = map(int, input().split())

board = [[0]*M for _ in range(N)]
count = [[0]*M for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(sx, sy):

    q = deque()
    q.append((sx,sy))
    count[sx][sy] = 1
    
    
    while q:
        x, y = q.popleft()
        
        if x == N-1 and y == M-1:
            break
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx and nx < N and 0<= ny and ny < M:
                if board[nx][ny] == 1 and count[nx][ny] == 0:
                    count[nx][ny] = count[x][y]+1
                    q.append((nx,ny))
                    
            
for i in range(N):
    row = input()
    for j in range(M):
        board[i][j] = ord(row[j])-48


bfs(0, 0)

print(count[N-1][M-1])








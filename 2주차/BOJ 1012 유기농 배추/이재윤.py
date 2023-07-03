// 파이썬에서 기본 재귀 제한은 1000이기 때문에,
// 이 부분에 대한 변경을 해줘야 한다 

import sys
sys.setrecursionlimit(10000)

T = int(input())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(x, y, N, M, board, visited):
    
    visited[x][y] = True
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<=nx and nx < N and 0<=ny and ny<M:
            if board[nx][ny] == 1 and visited[nx][ny] == False:
                dfs(nx, ny, N, M, board, visited)
    
    


for i in range(T):
    ans = 0
    
    M, N, K = map(int, input().split())
    
    board = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    
    for j in range(K):
        x, y = map(int, input().split())
        board[y][x] = 1
        
    for j in range(N):
        for k in range(M):
            if board[j][k] == 1 and visited[j][k] == False:
                ans += 1
                dfs(j, k, N, M, board, visited)
    
    print(ans)





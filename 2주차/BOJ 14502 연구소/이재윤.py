// 문제를 풀 때, 항상 시간 제한을 고려해야 한다 
// 순열로 풀어야 하는 것과 조합으로 풀어야 하는 것을 잘 구분해야 한다 

import sys
sys.setrecursionlimit(10**6)


maxRes = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def spread(tmpBoard, x, y, N, M, visited):
    
    visited[x][y] = True 
    
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<=nx and nx < N and 0<=ny and ny < M and tmpBoard[nx][ny] == 0 and visited[nx][ny] == False:
            tmpBoard[nx][ny] = 2 
            spread(tmpBoard, nx,ny,N,M, visited)
    
    
    



def getSafeZone(board, N, M):
    
    tmpBoard = [[0]*M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            tmpBoard[i][j] = board[i][j] 
            
            
    visited = [[False]*M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if visited[i][j] == False and tmpBoard[i][j] == 2:
                spread(tmpBoard, i, j, N, M, visited)
    

    safeArea = 0
    
    
    
    for i in range(N):
        for j in range(M):
            if tmpBoard[i][j] == 0:
                safeArea += 1 
    
    return safeArea 
    





def dfs(board, sx, sy, N, M, cnt):
    
    global maxRes 
    
    if cnt == 3:
        res = getSafeZone(board, N, M)
        maxRes = max(maxRes, res)
        return 
    
    
    for i in range(N):
        for j in range(M):
            if ((i==sx and j >= sy) or (i > sx)) and board[i][j] == 0:
                board[i][j] = 3
                dfs(board, i, j, N, M, cnt+1)
                board[i][j] = 0 


N, M = map(int, input().split())
board = [] 


for i in range(N):
    tmp = list(map(int, input().split()))
    board.append(tmp)
    

dfs(board, 0, 0, N, M, 0)
print(maxRes)

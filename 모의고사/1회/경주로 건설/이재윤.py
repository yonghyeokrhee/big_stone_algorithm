from collections import deque 

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
minCost = int(1e9)


def bfs(board, dir):
    
    N = len(board)
    
    costMap = [[int(1e9)]*N for _ in range(N)]
    
    q = deque()
    
    q.append([0, 0, 0, dir])
    
    
    while q:
        
        x, y, cost, dir = q.popleft() 
        
        if x == N-1 and y == N-1:
            continue    
        
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx and nx<N and 0<=ny and ny<N and board[nx][ny] == 0:
                
                if dir == i:
                    nCost = cost+100
                else:
                    nCost = cost+600
                
                
                if nCost < costMap[nx][ny]:
                    costMap[nx][ny] = nCost
                    q.append([nx, ny, nCost, i])
                
          
    
    return costMap[N-1][N-1]      
    

    
    
    
def solution(board):
    answer = 0
    
    N = len(board)
    minCost = min(bfs(board, 1), bfs(board, 2))
    
    answer = minCost
    
    return answer
    
    

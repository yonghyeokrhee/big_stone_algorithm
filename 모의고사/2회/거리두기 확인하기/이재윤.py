from collections import deque 

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y, board):
    
    visited = [[False]*5 for _ in range(5)]
    visited[x][y] = True
    q = deque()
    q.append([x, y, 0])
    
    rule = True 
    
    while q:
        x, y, dist = q.popleft() 
        
        if board[x][y] == 'P' and (dist == 1 or dist == 2):
            rule = False
            break 
            
        if dist == 2:
            continue
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx and nx < 5 and 0<= ny and ny<5 and visited[nx][ny] == False and board[nx][ny] != 'X':
                q.append([nx, ny, dist+1])
    
    
    return rule 



def solution(places):
    answer = []
    
    for place in places:
        board = [] 
        for j in range(0, 5):
            row = [] 
            for k in range(0, 5):
                row.append(place[j][k])
        
            board.append(row)
        
        people = [] 
        for i in range(0, 5):
            for j in range(0, 5):
                if board[i][j] == 'P':
                    people.append([i, j])
        total = True
        
        for person in people: 
            x = person[0]
            y = person[1]
            res = bfs(x, y, board)    
            if res == False:
                total = False
                break
        
        if total == True:
            answer.append(1)
        else:
            answer.append(0)
            
    return answer

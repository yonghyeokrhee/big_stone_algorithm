H, W = map(int, input().split())

board = []
dist = [[-1]*W for _ in range(H)]

for i in range(H):
    tmp = input()
    arr = []
    for c in tmp:
        arr.append(c)
    board.append(arr)
    
for i in range(H):
    for j in range(W):
        if board[i][j] == 'c':
            dist[i][j] = 0
            

for i in range(H):
    distance = -1 
    for j in range(W):
        if board[i][j] == 'c':
            distance = 0 
        else:
            if distance == -1:
                continue
            else:
                distance += 1 
                dist[i][j] = distance 
        
for i in range(H):
    for j in range(W):
        print(dist[i][j], end=' ')
    print('', end='\n')

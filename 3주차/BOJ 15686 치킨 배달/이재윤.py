N, M = map(int, input().split())

total = 0     
board = [] 
selected = [False]*20
houses = []
chickenHouses = [] 
minTotalDistance= int(1e9)

def getTotalDistance(): 
    
    totalDistance = 0 
    
    for i in range(len(houses)):
        
        chickenDistance = int(1e9)
        
        for j in range(total):
            if selected[j] == True:
                distance = abs(houses[i][0]-chickenHouses[j][0])+abs(houses[i][1]-chickenHouses[j][1])
                chickenDistance = min(chickenDistance, distance)

        totalDistance += chickenDistance     
    
    return totalDistance 

def dfs(pos, cnt):
    
    
    global total
    global M
    global minTotalDistance
    
    if cnt == M:
       totalDistance = getTotalDistance()
       minTotalDistance = min(minTotalDistance, totalDistance)    
    
    if pos == total:
        return 
        
    
    
    selected[pos] = True
    dfs(pos+1, cnt+1)
    selected[pos] = False
    dfs(pos+1, cnt)


for i in range(N):
    tmp = list(map(int, input().split()))
    board.append(tmp)
    
    
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            total += 1 
            

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            houses.append((i,j))
        if board[i][j] == 2:
            chickenHouses.append((i,j))


dfs(0, 0)

print(minTotalDistance)


    

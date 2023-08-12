N = int(input())

minCosts = list(map(int, input().split()))

board = []
selected = [False]*N
minCost = int(1e9)
ans = []

for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    
    
    
def dfs(pos, cnt):
    
    global minCost
    
    if cnt >= 1:
        cost = 0 
        p = 0
        f = 0
        s = 0
        v = 0
        
        for i in range(N):
            if selected[i] == True:
                p += board[i][0]
                f += board[i][1]
                s += board[i][2]
                v += board[i][3] 
                cost += board[i][4] 
        
        if p>=minCosts[0] and f >= minCosts[1] and s >= minCosts[2] and v >= minCosts[3] and minCost > cost:
            minCost = cost
            ans.clear()
            for i in range(N):
                if selected[i] == True:
                    ans.append(i+1)
            return 
                
    if pos == N:
        return 
    
    
    selected[pos] = True
    dfs(pos+1, cnt+1)
    selected[pos] = False 
    dfs(pos+1, cnt) 
    
    
    

dfs(0, 0)
    
if minCost == int(1e9):
    print(-1)
else:
    print(minCost)
    for num in ans:
        print(num,end=' ')
    
    
    
    
    

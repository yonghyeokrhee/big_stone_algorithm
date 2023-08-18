


N = int(input())

board = [] 

for i in range(N):
    row = list(map(int, input().split()))
    board.append(row) 
    
selected = [False]*N

minGap = int(1e9)

def getSum(team):
    
    sum = 0
    
    for i in range(0, len(team)):
        for j in range(i+1, len(team)):
            a = team[i]
            b = team[j]
            
            sum += board[a][b]
            sum += board[b][a]

    return sum 



def dfs(pos, cnt):
    
    global minGap
    
    if cnt == (N//2):
        
        teamA = []
        teamB = [] 
        
        for i in range(N):
            if selected[i] == True:
                teamA.append(i)
            else:
                teamB.append(i)
        
        sumA = getSum(teamA)
        sumB = getSum(teamB)
        gap = abs(sumA-sumB)
    
        minGap = min(minGap, gap)
    
        return 
    
    
    if pos == N:
        return 
    
    selected[pos] = True
    dfs(pos+1, cnt+1)
    selected[pos] = False
    dfs(pos+1, cnt)
    
    
    
    
dfs(0, 0)


print(minGap)
    

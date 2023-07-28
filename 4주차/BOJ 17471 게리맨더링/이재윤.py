// visited를 전역적으로 쓰는게 아니라, 지역적으로 쓰면서 매번 업데이트해야 한다

N = int(input())

arr = list(map(int, input().split()))

line = [[] for _ in range(N+1)]

selected = [False]*(N+1)

trueVisited = 0
falseVisited = 0
minDiff = int(1e9)

for i in range(N):
    tmp = list(map(int, input().split()))
    
    for j in range(1, len(tmp)):
        line[i+1].append(tmp[j])
        
        
def getDiff():
    
    trueSum = 0
    falseSum = 0
    
    for i in range(1, N+1):
        if selected[i] == True:
            trueSum += arr[i-1]
        if selected[i] == False:
            falseSum += arr[i-1]
            
    return abs(trueSum-falseSum)
    
    
def getTrueCnt(num, visited):
    
    global trueVisited
    
    visited[num] = True
    trueVisited += 1 
    
    for next in line[num]:
        if visited[next] == False and selected[next] == True:
            getTrueCnt(next, visited)
            

def getFalseCnt(num, visited):
    
    global falseVisited
    
    visited[num] = True
    falseVisited += 1 
    
    for next in line[num]:
        if visited[next] == False and selected[next] == False:
            getFalseCnt(next, visited)
    
      
def dfs(pos):
    
    global trueVisited
    global falseVisited
    global minDiff 
    
    if pos == N+1:
        trueCnt = 0
        falseCnt = 0 
        
        for i in range(1, N+1):
            if selected[i] == True:
                trueCnt += 1 
            if selected[i] == False:
                falseCnt += 1 
                
        if trueCnt == N or falseCnt == N:
            return 
        else:
            visited = [False]*(N+1)
            trueStart = 0
            falseStart = 0 
        
            
            for i in range(1, N+1):
                if selected[i] == True:
                    trueStart = i 
                    break 
            
            for i in range(1, N+1):
                if selected[i] == False:
                    falseStart = i
                    break
        
            trueVisited = 0
            falseVisited = 0
            getTrueCnt(trueStart, visited)
            
            getFalseCnt(falseStart, visited)
            
            if trueCnt == trueVisited and falseCnt == falseVisited:
                diff = getDiff()
                
                minDiff = min(minDiff, diff)
            
                
        return 
    
    
    selected[pos] = True
    dfs(pos+1)
    selected[pos] = False
    dfs(pos+1)
      
      
      
dfs(1)

if minDiff == int(1e9):
    print(-1)
else:
    print(minDiff)
        
        

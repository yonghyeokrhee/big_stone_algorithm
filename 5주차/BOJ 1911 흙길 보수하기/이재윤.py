

N, L = map(int, input().split())

info = []

for i in range(N):
    
    start, end = map(int, input().split())
    info.append((start, end))
    
    
info.sort(key=lambda x:x[0])
currEnd = 0 
total = 0 

for i in range(N):
    
    start = info[i][0]
    end = info[i][1] 
    
    if start <= currEnd:
        start = currEnd+1 
    else:
        currEnd = start-1
        
    ## print(start, end)
    if start>=end:
        continue
        
    length = end-start 
    cnt = 0 
    
    if length % L == 0:
        cnt = int(length // L)
    else:
        cnt = int(length / L) + 1 
        
    
    currEnd += cnt*L
    ## print(currEnd)
    total += cnt 
    
    
print(total)








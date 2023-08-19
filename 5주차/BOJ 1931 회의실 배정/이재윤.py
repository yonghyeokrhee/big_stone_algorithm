
N = int(input())

info = [] 

for i in range(N):    
    start, end = map(int, input().split())
    info.append((start, end))
    
    
info.sort(key=lambda x:(x[1], x[0]))

currEnd = info[0][1] 
cnt = 0 
cnt += 1 

for i in range(1, len(info)):
    if currEnd <= info[i][0]:
        cnt += 1 
        currEnd = info[i][1]
        
        
print(cnt)
        
    









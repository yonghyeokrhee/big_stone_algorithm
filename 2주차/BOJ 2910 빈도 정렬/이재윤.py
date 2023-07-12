// 메모리 초과가 나지 않도록, Dictionary를 활용하는 편이 좋다 

N, C = map(int, input().split())

arr = list(map(int, input().split()))
counts = {}
first = {}
check = [] 
data = [] 

for i in range(N):
    num = arr[i]
    
    if num in counts:
        counts[num] += 1 
    else:
        counts[num] = 1 
        
    if num in first:
        continue
    else:
        first[num] = i
        

for i in range(N):
    num = arr[i]
    if num not in check: 
        data.append((num, counts[num], first[num]))
        check.append(num) 

data.sort(key=lambda x:(-x[1], x[2]))

for i in range(len(data)):
    num = data[i][0]
    cnt = data[i][1]
    for j in range(cnt):
        print(num, end=' ')
    
    




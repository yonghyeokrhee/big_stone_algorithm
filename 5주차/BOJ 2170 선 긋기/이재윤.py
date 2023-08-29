// 25분

N = int(input())
arr = []

for i in range(N):
    
    a, b = map(int, input().split())
    arr.append((a,b))
    
arr.sort(key=lambda x:(x[0], x[1]))

start = arr[0][0]
end = arr[0][1]
total = end-start


for i in range(1, N):
    a, b = arr[i][0], arr[i][1]
    
    if a < end:
        if b <= end:
            continue
        elif b > end:
            total += (b-end)
            end = b
            
    elif a == end:
        total += (b-end)
        end = b
    
    elif a > end:
        total += b-a 
        start = a
        end = b 
    
    
print(total)

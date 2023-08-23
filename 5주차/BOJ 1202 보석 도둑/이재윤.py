import heapq 

N, K = map(int, input().split())

jew = []
for i in range(N):
    M, V = map(int, input().split())
    heapq.heappush(jew, (M,V))

bags = []

for i in range(K):
    num = int(input())
    bags.append(num)

bags.sort()

tmp_jew = [] 
ans = 0 

for bag in bags:
    
    while jew and bag>=jew[0][0]:
        heapq.heappush(tmp_jew, -heapq.heappop(jew)[1])
    
    if tmp_jew:
        ans -= heapq.heappop(tmp_jew)
    elif not jew:
        break
    
print(ans)


import sys
import heapq
input = sys.stdin.readline
n, k = map(int,input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
jew = sorted(arr , key=lambda  x: x[0])
b = [int(input()) for _ in range(k)] # 가방무게 배열
b = sorted(b)
answer = 0
cnt = 0
temp_q=[] # 보석의 가치만 기록하는 q
for i in b: # 용량이 작은 가방부터
    for a in arr: # 보석들을 순회하면서
        if jew and i >= a[0]: #보석의 무게가 가방보다 작으면
            heapq.heappush(temp_q, -heapq.heappop(jew)[1]) # 가방에 넣어둔다. 최대힙으로 사용하기 위해서 - 값으로 넣자.
    if temp_q:
        answer -= heapq.heappop(temp_q) # 가장 비싼 보석을 빼서 더한다.
        cnt +=1

    if cnt == k: # 모든 가방에 다 넣었으면 끝.
        break
print(answer)
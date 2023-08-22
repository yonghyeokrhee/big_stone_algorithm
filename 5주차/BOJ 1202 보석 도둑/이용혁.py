import sys
import heapq
input = sys.stdin.readline
n, k = map(int,input().split())
jew = []
for _ in range(n):
    heapq.heappush(jew, tuple(map(int, input().split())))
b = [int(input()) for _ in range(k)] # 가방무게 배열
b.sort()
answer = 0
temp_q=[] # 보석의 가치만 기록하는 q
for i in b: # 용량이 작은 가방부터
    while jew and i >= jew[0][0]: #가장 앞에 있는 보석의 무게가 가방보다 작으면
            a = heapq.heappop(jew)
            print(a)
            heapq.heappush(temp_q, (-a[1], a[1])) # 가방에 넣어둔다. 최대힙으로 사용하기 위해서 - 값으로 넣자.
    if temp_q:
        answer += heapq.heappop(temp_q)[1] # 가장 비싼 보석을 빼서 더한다.
    elif not jew:
        break
print(answer)
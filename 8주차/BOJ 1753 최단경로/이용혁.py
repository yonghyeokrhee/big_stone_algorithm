from collections import defaultdict
import heapq

V, E = map(int, input().split())
k = int(input())

d = defaultdict(list)
pq = []
dist = [float('inf')] * 20001

for _ in range(E):
    v, e, w = map(int, input().split())
    d[v].append((w,e))

heapq.heappush(pq,(0,k))
dist[k]=0
while len(pq):
    this = heapq.heappop(pq)
    here_dist = this[0]
    here = this[1]
    if dist[here] != here_dist: #  값이 없으면
        continue
    for there in d[here]:
        _dist = there[0]
        _there = there[1]
        if dist[_there] > dist[here] + _dist:
            dist[_there] = dist[here] + _dist
            heapq.heappush(pq,(dist[_there], _there))

for i in range(1,V+1):
    if dist[i] == float('inf'):
        print("INF")
    else:
        print(dist[i])
from collections import deque

N, K = map(int, input().split())
dist = [0] * 400001
visited = [0] * 400001
cnt = [0] * 400001


def BFS(x):
    depth = 0
    q: deque = deque()
    q.append(x)
    while q:
        for i in range(len(q.copy())):
            here = q.popleft()
            if here == K:
                print(here)
                return depth, cnt[here]
            if 0<= here <= 200000 and not visited[here]:
                print("this time going: ", here, " on depth: ", depth)
                visited[here] = True
                q.append(here + 1)
                dist[here+1] = dist[here] + 1
                cnt[here+1] += 1
                q.append(here-1)
                dist[here-1] = dist[here] + 1
                cnt[here-1] += 1
                q.append(here * 2)
                dist[here*2] = dist[here] + 1
                cnt[here*2] += 1
        depth +=1




if N == K:
    print(0)
    print(1)
else:
    d, c = BFS(N)
    print(d)
    print(c)
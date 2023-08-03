from collections import deque

N, K = map(int, input().split())
visited = [0] * 100001
cnt = [0] * 100001


def BFS(x):
    q: deque = deque()
    q.append(x)
    while q:
        here = q.popleft()
        if here == K:
            return visited[here], cnt[here]

        for there in [here+1,here-1,here*2]:
            if 0<= there <= 100000 and not visited[there]:
                visited[there] += visited[here] +1
                cnt[there] += cnt[here]
                q.append(there)
            elif 0<= there <= 100000 and visited[there] == visited[here] + 1:
                cnt[there] += cnt[here]


visited[N] = 1
cnt[N] = 1

if N == K:
    print(0)
    print(1)
else:
    d, c = BFS(N)
    print(d-1)
    print(c)
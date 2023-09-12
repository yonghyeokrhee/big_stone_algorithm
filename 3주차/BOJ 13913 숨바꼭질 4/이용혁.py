from collections import deque, defaultdict
N, K = map(int, input().split())
visited = [0] * 100001
tree = defaultdict(int)


def BFS(x):
    q: deque = deque()
    q.append(x)
    while q:
        here = q.popleft()
        if here == K:
            return visited[here]

        for there in [here+1,here-1,here*2]:
            if 0<= there <= 100000 and not visited[there]:
                visited[there] += visited[here] +1
                q.append(there)
                # print(f'append child {there} to parent {here}')
                tree[there] = here

visited[N] = 1



d = BFS(N)
path = []
for _ in range(d):
    path.append(K)
    K = tree[K]

print(d-1)
print(' '.join(map(str, path[::-1])))

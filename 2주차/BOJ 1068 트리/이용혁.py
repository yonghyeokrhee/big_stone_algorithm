from collections import deque, Counter

N = int(input())
arr = list(map(int, input().split()))

tree = [deque() for _ in range(N)]
for i, a in enumerate(arr):
    if a == -1:
        root = i
    else:
        tree[a].append(i)
cutter = int(input())
edges = [0] * N
def dfs(node):
    # 어떤 NODE를 제거했을 때 계속 들어가서 자신의 아래쪽으로 존재하는 모든 edge노드를 계산해두는 함수
    # edge가 있을 때 가장 밑에서만 더하기 할 수 있다.
    edges[node] = 0
    if not tree[node]: # edge인 경우
        edges[node] += 1
        return edges[node]
    else:
        childs = tree[node]
        for _ in range(len(childs)):
            c = childs.popleft()
            edges[node] += dfs(c)
        return edges[node]
dfs(root)

dups = Counter(edges)

if cutter == root:
    print(0)
elif edges[root] == edges[cutter]:
    print(1)
elif edges[cutter] == edges[arr[cutter]]:
    print(edges[root] - edges[cutter]+1)
else:
    print(edges[root] - edges[cutter])
from collections import deque

N = int(input())
arr = list(map(int, input().split()))

tree = [deque() for _ in range(N)]
for i, a in enumerate(arr):
    print(f'Node {i} has parent {a}')
    if a == -1:
        continue
    tree[a].append(i)
print(tree)

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
dfs(0)
print(edges[0] - edges[int(input())])
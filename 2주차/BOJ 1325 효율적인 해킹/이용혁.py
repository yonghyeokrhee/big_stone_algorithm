import sys
sys.setrecursionlimit(10000)

# def DFS(x):
#     ret = 1
#     visited[x] = 1
#     for truster in rel[x]:
#         if not visited[truster]:
#             ret += DFS(truster)
#     return ret


input = sys.stdin.readline
N, M = map(int, input().split())
rel = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    rel[b].append(a)

mx = 0
stack = []
arr = [0] * (N + 1)
for i in range(1, N + 1):
    visited = [0] * (N + 1)  # 초기화를 여기서 안해주면 안된다.. for 문 돌 때마다 초기화 되어야 함.
    stack.append(i)
    visited[i] = 1
    while stack:
        val = stack.pop()
        arr[i] +=1
        #leng = len(rel[i])
        for j in range(len(rel[val])):
            if len(rel[val]) > 0 and not visited[rel[val][j]]:
                stack.append(rel[val][j])
                visited[rel[val][j]] = True

mx = max(arr)
print(arr)
for i in range(1, N + 1):
    if arr[i] == mx:
        print(i, end=" ")
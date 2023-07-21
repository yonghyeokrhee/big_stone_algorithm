def DFS(x):
    ret = 1
    visited[x] = 1
    for truster in rel[x]:
        if not visited[truster]:
            ret += DFS(truster)
    return ret

# visited 안걸어 주니깐 무한 recursion이 들어가는 거 같다.

N,M=map(int,input().split())
rel = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int, input().split())
    rel[b].append(a) # dict 가 시간초과가 있어서 list 로 변경해서 해보자.
# dic_keys = list(dic.keys()) 이기 없앨 수 있고.
mx = 0
arr = [0] * (N + 1)
for i in range(1,N+1):
    visited = [0] * (N + 1) # 초기화를 여기서 안해주면 안된다.. for 문 돌 때마다 초기화 되어야 함.
    arr[i] = DFS(i)
    mx = max(mx,arr[i])

for i in range(1,N+1):
    if arr[i] == mx:
        print(i, end=" ")
from itertools import combinations
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

start = []
link = []
def dfs(index,path,k):
    if k == 0:
        start.append(path[:])
        link.append([i for i in range(1,N+1) if i not in path[:]])
        return
    for i in range(index, N):
        dfs(i+1, path+[i+1], k-1)
    return start, link

start, link = dfs(0,[],N//2)
mn = 1e+10
for s, l in zip(start, link):
    ss = 0
    for i in combinations(s,2):
        ss += arr[i[0]-1][i[1]-1] + arr[i[1]-1][i[0]-1]
    ls = 0
    for i in combinations(l,2):
        ls += arr[i[0]-1][i[1]-1] + arr[i[1]-1][i[0]-1]

    if abs(ss - ls) < mn:
        mn = abs(ss -ls)

print(mn)
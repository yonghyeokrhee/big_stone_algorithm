import sys

sys.setrecursionlimit(100000)

M, N, K = map(int, input().split())

loc = [[0, 2, 4, 4], [1, 1, 2, 5], [4, 0, 6, 2]]

arr = [[0] * N for _ in range(M)]

for _ in range(K):
    param = list(map(int, input().split()))
    x1, y1 = param[:2]
    x2, y2 = param[2:]
    for xx in range(x1, x2):
        for yy in range(y1, y2):
            arr[M - yy - 1][xx] = 1

def DFS(x, y) -> int:
    dy = [0, 1, 0, -1]
    dx = [-1, 0, 1, 0]
    ret = 1
    visited[y][x] = 1
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if (nx < 0) or (ny < 0) or (nx >= N) or (ny >= M):
            continue
        elif (arr[ny][nx] == 0) and (not visited[ny][nx]):
            ret += DFS(nx, ny)
    return ret


visited = [[0] * N for _ in range(M)]

ret = 0
vols = []
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0 and not visited[i][j]:
            vol = DFS(j, i)
            vols.append(vol)
print(len(vols), " ".join(str(v) for v in sorted(vols)))
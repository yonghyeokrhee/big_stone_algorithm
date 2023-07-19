import sys
sys.setrecursionlimit(10000)

N = int(input())

arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

def DFS(x, y, d):
    # 방문을 기록
    visited[y][x] = 1

    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if (ny < 0) or (nx < 0) or (ny >= N) or (nx >= N):
            continue
        if arr[ny][nx] > d and not visited[ny][nx]:
            # 잠기지 않은 곳을 돌아서 들어간다 DFS
            DFS(nx, ny, d)


answer = 1
for d in range(1, 100):
    ret = 0
    visited = [[0 for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[j][i] > d and not visited[j][i]:
                ret += 1
                DFS(i, j, d)
    answer = max(answer, ret)

print(answer)
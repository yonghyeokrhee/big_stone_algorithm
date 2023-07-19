N, d = 5, 4

# arr = [[0 for j in range(N)] for i in range(N)]
arr = [
    [6, 8, 2, 6, 2],
    [3, 2, 3, 4, 6],
    [6, 7, 3, 3, 2],
    [7, 2, 5, 3, 6],
    [8, 9, 5, 2, 7],
]



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


answer = 0
for d in range(1, 100):
    print("depth is: ",d )
    ret = 0
    visited = [[0 for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[j][i] > d and not visited[j][i]:
                ret += 1
                print("DFS started")
                DFS(i, j, d)
        print("safe region is: ", ret)
    answer = max(answer, ret)

print(answer)

# 모든 강수량 경우에 대해서 d를 테스트 해야 함 (d : 2 ~ 100)
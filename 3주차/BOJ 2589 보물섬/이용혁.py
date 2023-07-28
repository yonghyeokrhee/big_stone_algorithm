import itertools
from collections import deque
def BFS(x,y)->int:
    """
    주어진 위치에서 가장 멀리 갈 수 있는 육지까지의 거리를 측정하라
    종료조건이 필요한거 아닌가?
    array에다가 distance를 기록한 뒤에 가장 큰 값을 mx에다가 update해주면 됨.
    :param i:
    :param j:
    :return:
    """
    _mx = 0
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]

    q = deque()
    q.append((x,y))

    visited = [[0] * M for _ in range(N)]
    dist = [[0] * M for _ in range(N)]

    while q:
        x,y = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (ny>=0) and (nx>=0) and (ny < N) and (nx < M) and not visited[ny][nx] and arr[ny][nx] =='L':
                dist[ny][nx] = dist[y][x] + 1
                visited[ny][nx] = 1
                q.append((nx,ny))
                _mx = dist[ny][nx]
    return _mx


N,M = map(int,input().split())
arr = [[0] * M for _ in range(N)]

for r in range(N):
    for c, elem in enumerate(input()):
        arr[r][c] = elem

# for a in arr:
#     print(a)

mx = 0
for j in range(N):
    for i in range(M):
        if arr[j][i] == 'L':
            dist = BFS(i,j)
            #print(f"start from this {(i,j)}")
            #print(dist)
            mx = max(mx, dist)
print(mx)
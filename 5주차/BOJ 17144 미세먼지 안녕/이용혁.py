from collections import deque
R,C,T = map(int, input().split())
arr = [[*map(int,input().split())] for _ in range(R)]

# 공기 청정기 위치 파악하기 (상, 하)
air = [(y,x) for x in range(C) for y in range(R) if arr[y][x] ==-1]

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def expansion(arr):
    narr = [[0] * C for _ in range(R)]
    for y in range(R):
        for x in range(C):
            mise = arr[y][x] // 5
            if mise > 0:
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if ny < 0 or nx < 0 or ny > R-1 or nx > C-1 or arr[ny][nx] == -1:
                        continue
                    else:
                        narr[ny][nx] += mise
                        arr[y][x] -= mise

    for y in range(R):
        for x in range(C):
            narr[y][x] += arr[y][x]

    return narr

# 공기 청정기 바람 확산 로직 (위아래 각각 돌린다)
def rotation(arr):
    q = deque()
    y,x = air[0] # 위
    sy = 0
    sx = 0
    ey = y
    ex = C
    for i in range(sx, ex):
        q.append(arr[sy][i])
    for j in range(sy+1,ey+1):
        q.append(arr[j][i])
    for k in range(i - 1, -1, -1):
        if (j,k) == air[0]:
            arr[j][k] = 0
        q.append(arr[j][k])
    for n in range(j - 1, sy, -1):
        q.append(arr[n][k])
    q.rotate(-1)
    # 공기청정기 정화 & 회전
    for i in range(sx, ex):
        elem = q.popleft()
        arr[sy][i] = elem
    for j in range(sy+1, ey + 1):
        elem = q.popleft()
        arr[j][i] = elem
    for k in range(i - 1, -1, -1):
        elem = q.popleft()
        if (j,k) == air[0]:
            elem = -1
        arr[j][k] = elem
    for n in range(j - 1, sy, -1):
        elem = q.popleft()
        arr[n][k] = elem

    q = deque()
    y, x = air[1]  # 아래
    sy = y
    sx = x
    ey = R
    ex = C
    for i in range(sx, ex):
        if (sy, i) == air[1]:
            arr[sy][i] = 0
        q.append(arr[sy][i])
    for j in range(sy+1, ey):
        q.append(arr[j][i])
    for k in range(i - 1, -1, -1):
        q.append(arr[j][k])
    for n in range(j - 1, y, -1):
        q.append(arr[n][k])
    q.rotate(1)
    # 공기청정기 정화 & 회전
    for i in range(sx, ex):
        elem = q.popleft()
        if (sy, i) == air[1]:
            elem = -1
        arr[sy][i] = elem
    for j in range(sy+1, ey):
        elem = q.popleft()
        arr[j][i] = elem
    for k in range(i - 1, -1, -1):
        elem = q.popleft()
        arr[j][k] = elem
    for n in range(j - 1, y, -1):
        elem = q.popleft()
        arr[n][k] = elem
    return arr

for _ in range(T):
    arr = expansion(arr)
    arr = rotation(arr)

answer = 0
for ar in arr:
    for e in ar:
        if e > 0:
            answer += e

print(answer)

#시간 초과 문제 아직 해결 못함.

from collections import deque
N,L,R = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]
def check(ny,nx,y,x):
    """
    this 와 there 의 차이가 L 이상 R 이하인가
    :return: boolean 타입으로 반환한다.
    """
    global L, R
    if L <= abs(arr[y][x] - arr[ny][nx]) <= R:
        return True
    else:
        return False


def BFS(x,y)-> None:
    """
    하나로 이어진 부분을 찾는다.
    :return:
    """
    q=deque()
    q.append((x,y))
    c = [[0] * N for _ in range(N)]

    v[y][x] = 1
    c[y][x] = 1

    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    tot = arr[y][x]
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny< N and nx < N and nx >= 0 and ny >= 0 and not c[ny][nx] and check(ny,nx,y,x):
                v[ny][nx] = 1
                c[ny][nx] = 1
                q.append((nx,ny))
                tot += arr[ny][nx]
                cnt += 1

    flag = 0
    if cnt > 1:
        avg = int(tot / cnt)
        for j in range(N):
            for i in range(N):
                if c[j][i] == 1 and arr[j][i] != avg:
                    flag = 1
                    imigration[j][i] = avg

    return flag


flag = 1
ans  = 0
while flag:
    ret = 0
    v = [[0] * N for _ in range(N)]
    imigration = [[0] * N for _ in range(N)]
    # 연합국 조사하기
    for j in range(N):
        for i in range(N):
            if not v[j][i]:
                ret = max(BFS(i,j),ret)

    # 이민 하기
    for j in range(N):
        for i in range(N):
            if imigration[j][i]:
                arr[j][i] = imigration[j][i]

    flag = 1 if ret == 1 else 0

    if flag:
        ans += 1
print(ans)
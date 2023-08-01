N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

ret = 200 * 5 * 3 +1

def check(x,y):
    if visited[y][x]:
        return 0

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if (ny<0) or (nx<0) or (ny >= N) or (nx >= N) or visited[ny][nx]:
            return 0
    else:
        return 1 # able to set

def erase_flower(x,y):
    """
    모든 것을 되돌린다.
    :return:
    """

    visited[y][x] = 0

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        visited[ny][nx] = 0

def set_flower(x,y):

    visited[y][x] = 1
    price = arr[y][x]

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        visited[ny][nx] = 1
        price += arr[ny][nx]

    return price

def flower(num,hap):
    """
    실제로 꽃을 심는 것을 진행하는 함수
    :param x: 심어진 꽃의 개수
    :param y: 꽃을 심었을 때 드는 비용의 합계
    :return:
    """
    global ret
    if num == 3:
        ret = min(ret, hap)
        return

    for j in range(N):
        for i in range(N):
            if j < 0 or i < 0 or j >= N - 1 or i >= N - 1:
                continue
            else:
                if check(i, j):
                    flower(num+1, hap+set_flower(i,j))
                    erase_flower(i,j)


visited = [[0] * N for _ in range(N)]

flower(0,0)

print(ret)
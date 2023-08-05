#시간 초과 문제를 해결 하기 위해서 최대한 for 문을 효율적으로 사용하자.

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
                tot += arr[ny][nx]
                cnt += 1
                q.append((nx,ny))
                print(f"appending this location: ({nx},{ny})", arr[ny][nx])

    flag = 0

    avg = int(tot / cnt)
    print("total is: ",tot)
    print("num of united country is: ", cnt)
    print("average is: ", avg)

    #개선할 수 있는 부분을 찾았다.  (avg 계산하는 거 바꾸기)
    for j in range(N):
        for i in range(N):
            if c[j][i] == 1 and arr[j][i] != avg:
                flag = 1
                arr[j][i] = avg

    return flag
flag = 1
ans  = 0
while flag:
    ret = 0
    v = [[0] * N for _ in range(N)]
    for j in range(N):
        for i in range(N):
            if not v[j][i]:
                ret = max(BFS(i,j),ret)
    for ar in arr:
        print(ar)
    flag = 1 if ret == 1 else 0
    if flag:
        ans += 1
print(ans)
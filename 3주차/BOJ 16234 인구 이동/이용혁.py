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
        united.append([x,y]) # 연합국들을 여기에 저장해둔다. for 문 최소화하기 위해서.
        # 연합국들은 다음 round에서는 조사할 필요가 없다. 연합국들은 주변국들에 의해서만 병합될 뿐이기 때문이다.
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
    if cnt == 1:
        united.pop() # 하나 짜리 였다면 그냥 없애버리는게 맞다. 왜냐면 united는 전체 BFS에 대한 array이기 때문이다.
    elif cnt > 1: # 연합국이 두개 이상이라면
        flag = 1
        avg = int(tot / cnt)
        for _ in range(cnt):
            mig.append(avg)

    return flag

flag = 1
ans  = 0

while flag:

    ret = 0
    v = [[0] * N for _ in range(N)]

    imigration = [[0] * N for _ in range(N)]
    # 연합국 조사하기 -> 조사결과 좌표와 인구 저장해두자 (for 하나 더 줄일 수 있음)
    united = []
    mig = []
    for j in range(N):
        for i in range(N):
            if not v[j][i]:
                ret = max(BFS(i,j),ret)

    # 이민 하기
    for u,m in list(zip(united,mig)): #반드시 연합국이 있는 나라들에 대해서만 연산해야 한다. united와 mig의 길이가 같아야 한다.
        i, j = u
        arr[j][i] = m

    flag = 1 if ret == 1 else 0

    if flag:
        ans += 1
print(ans)
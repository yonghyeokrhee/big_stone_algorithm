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
    v[y][x] = 1

    dy = [-1,1,0,0]
    dx = [0,0,-1,1]

    while q:
        x, y = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny< N and nx < N and nx >= 0 and ny >= 0 and not v[ny][nx] and check(ny,nx,y,x):
                v[ny][nx] = 1
                q.append((nx,ny))

    # BFS 다 돌았으면 하나로 이어진 면적이 나올 것이다. 그것은 v 배열에 기록되었을 것이다.
    # v 배열에 1로 기록이 되어 있다면 arr 배열의 값들을 평균으로 바꾸어준다.
    flag = 0 # 아무런 값이 바뀌지 않은 것이 초기 값
    tot = 0
    cnt = 0
    for j in range(N):
        for i in range(N):
            if v[j][i] == 1: # 만약에 이어진 면적이 있으면 (모두 같은 값이 되어버리면 어떻게 되는건지 처리해야 한다)
                tot += arr[j][i]
                cnt += 1
    avg = int(tot / cnt)
    print("averaged is : ", avg)
    for j in range(N):
        for i in range(N):
            if v[j][i] == 1 and arr[j][i] != avg:
                arr[j][i] = avg # 값이 바뀔 필요가 있는 경우에만 값을 변환해준다.
                flag = 1 # 바뀌었으므로 1로 둔다.
    # 바뀐 부분이 있었는지를 확인한다.

    return flag
    # 모두 변경 완료.
flag = 1
while flag: # 더 이상 값이 변경되지 않을 때까지 작업을 계속 해준다.
    cnt = 0
    ret = 0
    v = [[0] * N for _ in range(N)]
    for j in range(N):
        for i in range(N):
            if not v[j][i]: # 방문한 곳이 아니라면 BFS를 시작하자.
                ret = max(BFS(i,j),ret) ## 좌상단에서부터 우측으로 BFS를 탐색하기 시작하자.
    # 이 작업이 모두 끝났다면 1일차에 있는 인구이동이 마무리 되는 것이다.
    print(arr)
    flag = 1 if ret == 1 else 0
    cnt += 1
print(cnt)

from collections import deque

q = deque()
N, M, K = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(N)]
rots = [[*map(int, input().split())] for _ in range(K)]

def rotation(r, c, s, rot):
    y = r - s - 1
    x = c - s - 1
    ey = r + s - 1
    ex = c + s - 1
    # q 만들기
    for i in range(x,ex+1):
        q.append(arr[y][i])
    for j in range(y + 1, ey+1):
        q.append(arr[j][i])

    for k in range(i - 1, x - 1, -1):
        q.append(arr[j][k])

    for n in range(j - 1, y, -1):
        q.append(arr[n][k])

    # 돌리기
    if rot:
        q.rotate(1)
    else:
        q.rotate(-1)

    # 회전 기록하여 마치기
    for i in range(x,ex+1):
        elem = q.popleft()
        arr[y][i] = elem
    for j in range(y + 1, ey+1):
        elem = q.popleft()
        arr[j][i] = elem
    for k in range(i - 1, x - 1, -1):
        elem = q.popleft()
        arr[j][k] = elem
    for n in range(j - 1, y, -1):
        elem = q.popleft()
        arr[n][k] = elem

def do_rotate(r,c,s,rot):
    while s:
        rotation(r,c,s,rot)
        s -= 1

sub_mn = 987654321
answer = []
def dfs(rots):
    """
    어레이의 최소합 *A를 구하는 함수  (*A 연산은 문제의 정의에 따른다)
    :param rots: rotation 좌표가 들어 있는 어레이
    :return: 어레이의 최소합 *A
    """
    global sub_mn
    if len(rots) == 0:
        for ar in arr:
            sarr = sum(ar)
            if sub_mn > sarr:
                sub_mn = sarr
        answer.append(sub_mn)

    for e in rots:
        next_rots = rots[:]
        next_rots.remove(e)
        r,c,s = e
        do_rotate(r,c,s,True)
        dfs(next_rots)
        do_rotate(r,c,s,False)

if __name__ == "__main__":
    dfs(rots)
    print(min(answer))
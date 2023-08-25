from collections import deque

q = deque()
N, M, K = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(N)]
rots = [[*map(int, input().split())] for _ in range(K)]

def rotation(r, c, s):
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
    q.appendleft(q.pop())
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

# rotation 반복하기 dfs 로 들어간다?
mn = 987654321
for r, c, s in rots:
    sub_mn = 987654321
    while s:
        ret = rotation(r, c, s)
        s -= 1
    for ar in arr:
        sarr = sum(ar)
        if sub_mn > sarr:
            sub_mn = sarr




print(mn)
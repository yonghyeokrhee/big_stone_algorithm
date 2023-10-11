N, M, K, C = map(int, input().split())
from collections import defaultdict
#2차원의 상태 [나무, 제초제 만기 시간] 혹은 각각의 1차원 array를 총 2개 가지고 한다 (후자 선택)
arr = [[*map(int,input().split())] for _ in range(N)]
ptime = [[0]*N for _ in range(N)]
dy = [0,1,0,-1]
dx = [1,0,-1,0]
answer = 0
# 성장

def count_something(x, y, some):
    some = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or nx < 0 or ny > N - 1 or nx > N - 1 or ptime[ny][nx] or arr[ny][nx] == -1:
            continue
        if some == 'free':
            if arr[ny][nx] == 0:
                some += 1
        elif some == 'tree':
            if arr[ny][nx] > 0:
                some +=1
    return some


def grow(arr):

    for y in range(N):
        for x in range(N):
            if ptime[y][x] or arr[y][x] <= 0:
                continue
            arr[y][x] += count_something(x,y,'tree') # todo: 주변의 나무 개수를 count 하여 더해준다.
    return arr

def expansion(arr):
    narr = [[0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if ptime[y][x]:
                continue
            free = count_something(x,y,'free')
            if not free:
                continue
            rep = arr[y][x] // free #todo: 실제 주변에 번식 가능여부를 cnt 한다.
            if rep > 0:
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if ny < 0 or nx < 0 or ny > N-1 or nx > N-1  or ptime[ny][nx] or arr[ny][nx] > 0 or arr[ny][nx] == -1:
                        continue
                    else:
                        narr[ny][nx] += rep

    for y in range(N):
        for x in range(N):
            if ptime[y][x]:
                continue
            narr[y][x] += arr[y][x]

    return narr

dy2 = [1,-1,-1,1] # 대각선 움직임
dx2 = [1,-1,1,-1]


def reset_pest():
    for y in range(N):
        for x in range(N):
            if ptime[y][x]:
                ptime[y][x] -= 1

def check(arr,k)->list:
    global answer
    mx = 0
    mx_x = 1
    mx_y = 1
    d = defaultdict(list)
    for y in range(N):
        for x in range(N):
            if ptime[y][x] or arr[y][x] <= 0:
                continue
            cut = 0
            cut += arr[y][x]
            for i in range(4):
                for kk in range(1, k + 1):
                    ny = y + dy2[i] * kk
                    nx = x + dx2[i] * kk
                    if ny < 0 or nx < 0 or ny > N - 1 or nx > N - 1 or ptime[ny][nx] or arr[ny][nx] <= 0:
                        break
                    cut+=arr[ny][nx]
            if mx < cut:
                mx = cut
                mx_x = x
                mx_y = y

    return mx, mx_x, mx_y

def eliminate(arr,k):
    global answer

    count, x,y = check(arr,k) # 제초제를 뿌릴 위치를 찾는다.
    if not count:
        return arr # 종료
    answer += count

    ptime[y][x] = C
    for i in range(4):
        for kk in range(1, k + 1):
            ny = y + dy2[i]*kk
            nx = x + dx2[i]*kk
            if ny < 0 or nx < 0 or ny > N - 1 or nx > N - 1 or arr[ny][nx] == -1:
                break
            if arr[ny][nx] == 0:
                ptime[ny][nx] = C
                break
            ptime[ny][nx] = C
    return arr


for m in range(M):

    arr = grow(arr) # 성장한다.
    arr = expansion(arr) # 번식한다.
    reset_pest() # pest 의 수명을 -1 감소시킨다.
    arr = eliminate(arr,K) # 제초제를 뿌린다.

print(answer)
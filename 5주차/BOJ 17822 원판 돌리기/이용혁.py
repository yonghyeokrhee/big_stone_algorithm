import copy
from collections import deque
N, M, T = map(int, input().split())

arr = []
for i in range(N):
    arr.append(deque(map(int,input().split())))


for _ in range(T):
    x,d,k = map(int, input().split())

    for i in range(N):
        if not (i+1)%x and not d:
            #print(i)
            arr[i].rotate(k)
        if not (i+1)%x and d:
            #print(i)
            arr[i].rotate(-k)

    _arr = copy.deepcopy(arr)

    tot = 0
    cnt = 0
    flag = True
    for j in range(N):
        for i in range(M):
            tot += arr[j][i] if str(arr[j][i]).isdigit() else 0
            cnt += 1 if str(arr[j][i]).isdigit() else 0
            if arr[j][i] != '#' and arr[j][i-1]!='#' and arr[j][i] == arr[j][i-1]:
                flag = False # 한번이라도 삭제 된 경우.
                _arr[j][i] = '#'
                _arr[j][i-1] = '#'
            if j<N-1 and arr[j][i] != '#' and arr[j+1][i]!='#' and arr[j][i] == arr[j+1][i]:
                flag = False # 한번이라도 삭제 된 경우.
                _arr[j][i] = '#'
                _arr[j+1][i] = '#'

    # 아무일도 일어나지 않은 경우 처리
    #print("flag is : ", flag)
    if flag and cnt:
        avg = tot / cnt
        #print(avg)
        for j in range(N):
            for i in range(M):
                if arr[j][i] == '#':
                    continue
                elif arr[j][i] < avg:
                    arr[j][i] +=1
                elif arr[j][i] > avg:
                    arr[j][i]-=1
    else:
        arr = copy.deepcopy(_arr)

    # for a in arr:
    #     print(a)

# 정답 처리
answer = 0
for j in range(N):
    for i in range(M):
        if str(arr[j][i]).isdigit():
            answer += arr[j][i]
print(answer)


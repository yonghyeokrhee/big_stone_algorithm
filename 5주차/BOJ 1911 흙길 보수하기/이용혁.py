N, L =  map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(N)]
arr.sort(key = lambda x: x[0]) # 먼저 웅덩이 시작점을 기준으로 한다.
s,e, cnt = 0,0,0
for elem in arr:
    if e < elem[0]:
        s = elem[0]
        e = s
        if not (elem[1] - s) % L:
            cnt += (elem[1] - s) // L
            e = elem[1]
        else:
            cnt += (elem[1] - s) // L + 1
            e = elem[1] - (elem[1] - s) % L + L
    elif s <= elem[0] <= e:
        if not (elem[1] - e) % L:
            cnt += (elem[1] - e) // L
            e = elem[1]
        else:
            cnt += (elem[1] - e) // L + 1
            e = elem[1] - (elem[1] - e) % L + L
print(cnt)


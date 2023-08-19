n = int(input())
arr = list(map(int, input().split()))
k = int(input())

mem = [0] * 1000001 # 1백만 1 이하로만 기록해도 된다. 그 이상은 기록 할 필요가 없음.

cnt = 0
for i in arr:
    if k-i >= 1000001:
        continue
    elif mem[k-i]:
        cnt += 1
    else:
        mem[i] = 1
print(cnt)
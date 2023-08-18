n = int(input())
arr = list(map(int, input().split()))
k = int(input())

mem = [0] * 1000001 # 1백만 1 이하로만 기록해도 된다. 그 이상은 기록 할 필요가 없음.

## 200만 보다 큰 수에 대해 x 값이 제시되었을 때 예외 처리 해보기.

cnt = 0
for i in arr:
    if mem[k-i]:
        cnt += 1
    else:
        mem[i] = 1
print(cnt)
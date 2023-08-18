n = int(input())
arr = [*map(int,input().split())]

mem = [0] * 100001
# 가장 멀리갈 수 있는 unique 한 배열의 끝을 찾아본다.

# line sweeping style 문제
cnt = 0
flag = False
for j in range(n):
    for i in range(j,n):
        if not mem[arr[i]]:
            mem[arr[i]] = 1 # 없으면 채운다.
            if (i-j) + 1 == n-j:
                flag = True
                break
        else:
            cnt += (i-j) # 겹치지 않고 이동한 최장 거리를 기록한다.
            mem[arr[j]] = 0  # 10만 이하에 해당하는 수를 저장하기. 단, break가 되면 갱신한다.
            break
    if flag:
        break
k = n-j
cnt += (k * (k+1) ) // 2

print(cnt)


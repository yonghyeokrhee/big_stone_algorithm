from collections import deque
K = int(input())
arr = [deque([*map(int, list(input()))]) for _ in range(K)]
n = int(input())
rots = [[*map(int, input().split())] for _ in range(n)]

# for i in arr:
#     print(i)
#
# for i in rots:
#     print(i)

# 왼쪽 돌리기 구현

for elem, d in rots:
    l,r = arr[elem-1][-2], arr[elem-1][2]
    # 3번의 오른쪽 왼쪽에 대한 돌리기를 구현한다.
    # 왼쪽
    if elem-2 <= 0 or l == arr[elem-2][2]: # 극이 같으면 (혹은 왼쪽 끝)
        if elem >= K or r == arr[elem][-2]: #극이 같으면 (혹은 오른쪽 끝)
            continue # 양쪽 모두 그대로
        else: # 오른쪽에 돌릴 것이 있다면
            arr[elem].rotate(-d)  # 반대쪽으로 회전 시킨다
    else:
        arr[elem-2].rotate(-d) # 반대쪽으로 회전 시킨다

    arr[elem-1].rotate(d) # elem 번째 톱니를 direction으로 회전한다. 한 번.

    # print("========rotation ends =========")
answer = 0
for i in arr:
    if i[0] == 1:
        answer += 1
print(answer)
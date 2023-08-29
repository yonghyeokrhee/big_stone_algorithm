from collections import deque
K = int(input())
arr = [deque([*map(int, list(input()))]) for _ in range(K)]
n = int(input())
rots = [[*map(int, input().split())] for _ in range(n)]

for i in arr:
    print(i)

# for i in rots:
#     print(i)

def go(elem,r):
    if r: # 오른쪽 확인
        # print(elem)
        if elem+1 >= K or arr[elem][2] == arr[elem + 1][-2]:
            return False
        else:
            go(elem+1,r)
            arr[elem+1].rotate(-d)  # 반대쪽으로 회전 시킨다
    else: # 왼쪽 확인
        if elem - 2 <= 0 or arr[elem][-2] == arr[elem -1][2]:
            return False
        else:
            go(elem -1,r)
            arr[elem -1].rotate(-d)  # 반대쪽으로 회전 시킨다



def do_rotate(elem,d)->bool:
    """조건을 확인하고 돌리는 함수"""
    go(elem-1, True) #오른쪽
    go(elem-1, False) #왼쪽
    arr[elem - 1].rotate(d) # 자신을 회전한다.

# 왼쪽 돌리기 구현
flag=0
for elem, d in rots:
    flag += 1
    print(f"this time {flag} is executed")
    do_rotate(elem,d)
    print("========rotation ends =========")
    for i in arr:
        print(i)

print("answer is ....")

answer = 0
for i in arr:
    if i[0] == 1:
        answer += 1
print(answer)
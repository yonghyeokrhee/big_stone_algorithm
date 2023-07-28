from itertools import permutations
from collections import deque
N:int = int(input())
operator:list = input().split()

nums = [i for i in range(10)]


mx = 0
mn = 10000000000

def DFS(c,operator):
    """
    c : deque 자료형으로 된 n개의 숫자
    operator : deque 자료형으로 된 n-1개의 부등호
    만약에 부등호 조건이 맞지 않으면 바로 포기하는 백트레킹을 집어 넣어보자.
    :return: 만약 끝까지 모두 부등호를 만족한다면 true 아니라면 false 값이 될 예정
    """

    if not c and not operator:
        return True

    operation.append(operator.popleft())
    operation.append(str(c.popleft()))

    if eval(''.join(operation)):

        # 숫자와 부등호, 그리고 그 다음 숫자가 True 라면
        return DFS(c,operator)
    else: # 위 단계를 통과 하지 못한다면 (backtracking)
        return False

# c= (9,5,6,7,8,4,3,0,1,2)
# cc = deque((9,5,6,7,8,4,3,0,1,2))
# op = deque(operator)
# operation = [str(cc.popleft())]
# if DFS(cc, op): # True 이면
#     string_num = int("".join(map(str,c)))
#     num = int(string_num)
#     mx = max(mx, num)
#     mn = min(mn, num)
# print(str(mx), str(mn) if mn > 100 else '0'+str(mn))

for c in permutations(nums,N+1):
    cc = deque(c)
    op = deque(operator)
    operation = [str(cc.popleft())]
    if DFS(cc, op): # True 이면
        string_num = int("".join(map(str,c)))
        num = int(string_num)
        mx = max(mx, num)
        mn = min(mn, num)
print(str(mx), str(mn) if mn > 100 else '0'+str(mn))
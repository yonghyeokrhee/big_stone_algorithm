from itertools import permutations
from itertools import chain
from collections import deque
N:int = int(input())
operator:list = input().split()

nums = [i for i in range(10)]


mx = 0
mn = 10000000000

result = []

def DFS(perm):
    if len(perm) == 0:
        result.append(prev_elem)

    for n in perm:

        next_elem = perm.copy()
        next_elem.remove(n)
        prev_elem.append(str(n))

        operation.append(op.popleft())
        op_string = prev_elem[0] + ''.join(list(chain.from_iterable(zip(operation,prev_elem[1:]))))
        print(op_string)
        if eval(op_string):
            DFS(next_elem)
            prev_elem.pop()
        else:
            print(f"Finished with {prev_elem}")
            prev_elem.pop()

for i in nums:
    q = deque(nums)
    op = deque(operator)
    operation = []
    q.remove(i)
    prev_elem = []
    prev_elem.append(str(i))
    DFS(q)

print(result)
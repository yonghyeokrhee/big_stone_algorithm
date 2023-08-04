from collections import deque
from itertools import permutations
N = int(input())
arr = list(map(int, input().split()))
attack = [9,3,1]
depth = 0

def BFS(arr):
    global depth
    q = deque()
    q.append(arr)
    while q:
        l = len(q.copy())
        for _ in range(l):
            this = q.popleft()
            if sum(this) == 0:
                return depth
            for p in permutations(attack[:N]):
                q.append([max(scv-a,0) for scv, a in zip(this,p)])

        depth +=1

print(BFS(arr))
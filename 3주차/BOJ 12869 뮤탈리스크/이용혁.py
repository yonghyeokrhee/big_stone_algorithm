from collections import deque
from itertools import permutations

N = int(input())
inp = list(map(int, input().split()))
arr = [0, 0, 0]
for i in range(N):
    arr[i] = inp[i]

v = [[[0] * 64 for _ in range(64)] for _ in range(64)]
attack = [9, 3, 1]


def BFS(arr):
    q = deque()
    q.append(arr)
    while q:
        l = len(q.copy())
        for _ in range(l):
            this = q.popleft()
            if sum(this) == 0:
                return v[this[0]][this[1]][this[2]]
            for p in permutations(attack[:N]):
                hp = [max(scv - a, 0) for scv, a in zip(this, p)] + [0] * (3 - len(p))
                if not v[hp[0]][hp[1]][hp[2]]:
                    v[hp[0]][hp[1]][hp[2]] = v[this[0]][this[1]][this[2]] + 1
                    q.append(hp)


v[arr[0]][arr[1]][arr[2]] += 1
print(BFS(arr) - 1)
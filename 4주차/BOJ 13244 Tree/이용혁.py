# 위상정렬로 connectedness 확인할 수 있다. -> 실패
# 중위순회가 가능해야 한다.
import copy
from collections import defaultdict
T = int(input())


def dfs(node):
    v[node] = 1
    for n in d[node]:
        if not v[n]:
            dfs(n)

for _ in range(T): # 테스트케이스
    v = [0] * 1000000
    d = defaultdict(list)
    V = int(input())
    E = int(input())
    for _ in range(E):
        a, b = map(int, input().split())
        d[a].append(b)
        d[b].append(a)  # 양방향 간선

    if E != V-1:
        print("graph")
    else:
        dfs(1)
        success = True
        for i in range(1,V+1):
            if v[i] == False:
                success = False

        if success:
            print("tree")
        else:
            print("graph")

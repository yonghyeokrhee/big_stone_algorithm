from collections import defaultdict
from itertools import combinations
n = int(input())
pop = list(map(int, input().split()))
pop.insert(0,0) # 배열을 노드 인구로 사용하기 위해서 index를 한칸씩 이동

graph = defaultdict(list)

# 양방향 간선 그래프
for i in range(1,n+1):
    node = list(map(int, input().split()))
    graph[i] = node[1:]

# print(graph)


def DFS(city, value)-> list:
    """
    시작점에서부터 하나로 이어진 그래프를 찾아낸다.
    :return: tuple(size, sum of population)
    """
    v[city] = 1
    ret = [1, pop[city]]
    for there in graph[city]:
        if comp[there] != value:
            continue
        if v[there]:
            continue
        _temp = DFS(there, value)
        ret[0] += _temp[0]
        ret[1] += _temp[1]

    return ret

# def DFS(city)-> tuple:
#     """
#     시작점에서부터 하나로 이어진 그래프를 찾아낸다.
#     :return: tuple(size, sum of population)
#     """
#     global size, population
#     v[city] = 1
#     sec = comp[city] # city의 section (1 또는 0 이다)
#     #if graph[city]
#     # base case
#     # if v[nc]:# 더 이상 진행이 어렵다면
#     #     return 1, pop[nc] # size 1과 자신의 인구값인 population을 반환한다.
#     for nc in graph[city]:
#         if nc <= 0 and comp(nc) != sec and v[nc]:
#             continue
#         else:
#             size += 1
#             population += pop[nc]
#             DFS(nc)
#
#     return size, population

# 1. combination(bit masknig) 으로 connected component를 만든다.
# bitmasking으로 하거나 그냥 combination으로 구현해도 된다.

ret = 1e+10

for i in range(1,1<<n-1):
    v = [0] * (n+1)  # 탐색에 사용할 visited 배열
    comp = defaultdict(int)
    size = population = 0 # 각각 다른 주소로 0 assign
    for j in range(n):
        if (i & (1 << j)):
            last_comp1 = j+1
            comp[j+1] = 1
        else:
            last_comp2 = j+1
            comp[j+1] = 0

    # print(comp)

    s1, p1 = DFS(last_comp1, 1) # 1에서 출발하여 1로 시작하는 영역의 size와 population을 구하는 함수
    s2, p2 = DFS(last_comp2, 0) # 0에서 출발하여 1로 시작하는 영역의 size와 population을 구하는 함수
    if s1 + s2 != n: # 두개의 cc 로 분할되지 않은 경우의 수 이므로 무시한다.
        continue
    else:
        ret = min(ret, abs(p2-p1))
        # print(f"this time min value is: {ret}")
        # assert ret != 13
if ret == 1e+10:
    print("-1")
else:
    print(ret)  # 두 도시의 인구 차이

    # print(f"size of connected component {comp[1]} is :", s)
    # print("pop of section 1 is: ", p)

# 2. 두 node를 선택하고 두 node에서 시작한 선거구역이 두 개의 연결된 선거구로 끝나는지 확인한다.



import itertools

N,M = map(int,input().split())

house = []
chicken = []

for r in range(N):
    for index, elem in enumerate(list(map(int,input().split()))):
        if elem == 1:
            house.append((r,index))
        elif elem == 2:
            chicken.append((r,index))

chicken_n = list(itertools.combinations(chicken,M))

min_result = 100000000
for comb in chicken_n:
    res = 0
    for h in house:
        _min = 1000
        for c in comb:
            dist = abs(h[0] - c[0]) + abs(h[1]-c[1])
            _min = min(_min, dist)
        res += _min
    min_result = min(min_result,res)
print(min_result)
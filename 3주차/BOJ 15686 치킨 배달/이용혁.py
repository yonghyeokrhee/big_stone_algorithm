import itertools

N,M = map(int,input().split())

#arr=[list(map(int,input.split()) for _ in range(N))]

house = []
chicken = []

for r in range(N):
    for index, elem in enumerate(list(map(int,input().split()))):
        if elem == 1:
            house.append((r,index))
        elif elem == 2:
            chicken.append((r,index))

# print(house)
# print(chicken)
chicken_n = list(itertools.combinations(chicken,M))
# print(chicken_n)

min_result = 100000000
for comb in chicken_n:
    #print("this combination is: ",comb)
    res = 0
    for h in house:
        _min = 1000
        for c in comb:
            dist = abs(h[0] - c[0]) + abs(h[1]-c[1])
            _min = min(_min, dist)
        #print(f"minimum chicken distance for house {h} is: ", _min)
        res += _min
    min_result = min(min_result,res)
    #print("sum of chicken distance for this combination is: ",res)
print(min_result)
# 비트마스킹으로 combination을 구현하는 것이 핵심인 문제이다.
# 따라서 먼저 비트마스킹으로 combination을 작성하는 연습 먼저 해보자.
from collections import defaultdict
import math
n = int(input())
a = defaultdict(list)
ret = defaultdict(list)
# 1번부터 amx 15번까지 dict를 채운다.
mp, mf, ms, mv = map(int, input().split())
#print(mp, mf, ms, mv)
for k in range(n):
    a[k+1] = list(map(int, input().split()))

min_cost = math.inf

for i in range(1<<n):
    protein, fat, carbo, vitamin, cost = 0, 0, 0, 0, 0
    choice = []
    for j in range(n):
        if (i & (1 << j)):
            food = a[j+1]
            protein+=food[0] #protein
            fat += food[1] #fat
            carbo += food[2] #carbo
            vitamin += food[3] #vitamin
            cost += food[4] #cost
            choice.append(j+1)
    if protein >= mp and fat >= mf and carbo >= ms and vitamin >= mv:
        if min_cost >= cost:
            min_cost = cost
            ret[cost].append(choice)

if not ret:
    print(-1)
else:
    print(min_cost)
    print(" ".join(map(str, sorted(ret[min_cost])[0])))
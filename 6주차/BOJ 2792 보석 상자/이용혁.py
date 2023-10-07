from itertools import combinations_with_replacement
from collections import Counter
#조합 문제

boy, lux = map(int,input().split())
arr = [int(input()) for _ in range(lux)]
answer_min = int(10e9)
for i in combinations_with_replacement(range(lux),boy):
    counter = Counter(i)
    if len(counter.keys())<lux:
        continue
    jealous_mx=0
    for k,l in zip(counter.keys(),arr):
        argmax = l//counter[k] if l%counter[k] ==0 else l//counter[k] + 1
        jealous_mx = max(jealous_mx, argmax)
    answer_min = min(answer_min,jealous_mx)
print(answer_min)
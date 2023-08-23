from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    answer = []
    for n in course:
        mx_comb=defaultdict(list)
        mycomb = defaultdict(int)
        mx = 0
        for o in orders:
            for i in combinations(o,n):
                i = sorted(list(i))
                i = tuple(i)
                mycomb[i] +=1
                if mycomb[i] >= mx and mycomb[i]>=2:
                    mx = mycomb[i]
                    mx_comb[mx].append(i)
        for i in mx_comb[mx]:
            answer.append("".join(i))
    return sorted(answer)
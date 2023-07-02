from collections import defaultdict
tc = int(input())
for _ in range(tc):
    mydict = defaultdict(int)
    n = int(input())
    for i in range(n):
        outfit = input().split()
        mydict[outfit[1]] += 1
    answer = 1
    for v in mydict.values():
        answer *= (v+1)
    print(answer-1)

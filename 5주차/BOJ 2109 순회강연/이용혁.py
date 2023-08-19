from collections import defaultdict
from queue import PriorityQueue
n = int(input())

mydict = defaultdict(list) # key를 날짜, value를 강연료로 하는 dictionary
q = PriorityQueue()

for _ in range(n):
    v,key= map(int, input().split())
    mydict[key].append(v)

keys = sorted(list(mydict.keys()))
for k in keys:
    lecs = mydict[k]
    i = 0
    while True:
        q.put(lecs[i])
        if q.qsize() > k:
            q.get()
        i += 1
        if i == len(lecs):
            break

ret = 0
for i in range(q.qsize()):
    ret += q.get() # 작은 순서대로 꺼내는 HQ
print(ret)
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
    if len(lecs)==1 and k-1>=0: # size가 하나뿐이면 우선 그자리에 넣는다.
        q.put(lecs[-1])
    else: # size가 하나 이상이면 앞쪽 일정과 비교하여 강연을 갈 수 있다. q가 이미 꽉 차 있다면 q에다가 집어넣고 가장 작은 것을 뺄 수 있다.
        i = 0
        while True: #mem[k-1] < lecs[i] and k-1>=0:
            if q.qsize() < k:
                q.put(lecs[i])
            elif q.qsize() >= k:
                q.put(lecs[i])
                q.get() #하나 넣고 가장 작은 걸 하나 뺀다.
            i += 1
            if i == len(lecs):
                break

ret = 0
for i in range(q.qsize()):
    ret += q.get() # 작은 순서대로 꺼내는 HQ
print(ret)
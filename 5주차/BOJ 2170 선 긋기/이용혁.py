K = int(input())
arr = [[*map(int, input().split())] for _ in range(K)]
ret = []
s = +1000000000
e = -1000000000

arr = sorted(arr,key = lambda x: (x[0],x[1])) # 정렬

ret = []
for i in arr:
    ns, ne = i
    if ns < s and ne > s:
        s = ns # start가 작으면 update
    if ne > e and ns < e:
        e = ne # end가 크면 update
    if (ne < s) or (e<ns): # 완전히 새롭게 시작하면
        ret.append((s,e)) # 기존것은 넣어두자.
        s , e = ns, ne

ret.append((s,e)) # 마지막 결과 저장
answer = 0
for i in range(len(ret)):
    if i == 0:
        continue
    else:
        line = ret[i]
        answer+=abs(line[1] - line[0])
print(answer)
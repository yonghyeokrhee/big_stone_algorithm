import sys
input = sys.stdin.readline
K = int(input())
arr = [[*map(int, input().split())] for _ in range(K)]
ret = []

arr = sorted(arr,key = lambda x: (x[0])) # 정렬
s = arr[0][0]
e = arr[0][1]

ret = []
for i in arr:
    ns, ne = i
    if ne <= e:
        continue
    if ne > e and ns <= e:
        e = ne # end 만 업데이트
    if ns > e:
        ret.append((s,e))
        s , e = ns, ne

ret.append((s,e)) # 마지막 결과 저장
answer = 0
for i in range(len(ret)):
    line = ret[i]
    answer+=abs(line[1] - line[0])
print(answer)
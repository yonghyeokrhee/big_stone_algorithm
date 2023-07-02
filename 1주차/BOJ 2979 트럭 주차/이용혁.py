import sys
ps = [list(map(int, data.split())) for data in sys.stdin.readlines()]

bucket = [0] * 100
for t in range(ps[1][0], ps[1][1]):
    bucket[t] += 1

for t in range(ps[2][0], ps[2][1]):
    bucket[t] += 1

for t in range(ps[3][0], ps[3][1]):
    bucket[t] += 1

answer= 0
for i in bucket:
    if i == 1:
        answer += i * ps[0][0]
    if i == 2:
        answer += i * ps[0][1]
    if i == 3:
        answer += i * ps[0][2]
print(answer)

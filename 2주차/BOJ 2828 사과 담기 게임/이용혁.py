N, M = map(int, input().split())
J = int(input())

loc = 1
move = 0
for _ in range(J):
    end = loc + M -1
    a = int(input())
    if (a >= loc) and (a <= end):
        continue
    elif a > end:
        move += a - end
        loc += a - end
    elif loc > a:
        move += loc - a
        loc = a

print(move)
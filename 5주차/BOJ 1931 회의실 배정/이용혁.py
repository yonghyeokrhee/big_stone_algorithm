n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

arr = sorted(arr, key = lambda x: (x[1],x[0]))

line = cnt = 0
for a in arr:
    if line <= a[0]:
        line = a[1]
        cnt += 1
        print(a)
    elif line > a[0]:
        continue

print(cnt)
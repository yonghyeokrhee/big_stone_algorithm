N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 도착시간 기준으로 정렬
arr = sorted(arr, key = lambda x : x[0])

line = 0
for elem in arr:
    if elem[0] >= line:
        line_start = elem[0]
        line = line_start + elem[1]

    elif elem[0] < line:
        line_start = line
        line = line_start + elem[1]

print(line)
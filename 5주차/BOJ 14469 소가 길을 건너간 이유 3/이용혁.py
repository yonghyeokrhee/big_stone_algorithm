N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 도착시간 기준으로 정렬
arr = sorted(arr, key = lambda x : x[0])

line = 0
for elem in arr:
    line = max(line, elem[0]) + elem[1]
print(line)
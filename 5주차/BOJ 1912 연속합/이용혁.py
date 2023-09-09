n = int(input())
arr = [*map(int, input().split())]
answer = []*n
mx = -9876754321
for i in range(1,n):
    if arr[i-1] > mx:
        mx = arr[i-1]
    if arr[i-1] < 0:
        continue
    else:
        arr[i] = arr[i] + arr[i-1]

if arr[n-1] > mx:
    mx = arr[n-1]

print(mx)
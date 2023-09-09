n = int(input())
arr = [*map(int, input().split())]
answer = []*n
mx = arr[0]
for i in range(1,n):

    if arr[i-1] < 0:
        pass
    else:
        arr[i] = arr[i] + arr[i-1]
    if arr[i] > mx:
        mx = arr[i]

print(mx)
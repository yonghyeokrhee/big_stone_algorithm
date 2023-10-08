ret = 10e18
boy, lux = map(int,input().split())
arr = [int(input()) for _ in range(lux)]

def check(mid):
    num = 0
    for i in range(lux):
        num += arr[i] / mid + 1 if arr[i] % mid else arr[i] /mid
    return boy >= num

lo = 1
hi = max(arr)
while lo <= hi:
    mid = int((lo + hi) /2) # c++에서 그대로 옮기면서 실수가 있었던 부분
    if check(mid):
        ret = min(ret,mid)
        hi = mid -1
    else:
        lo = mid + 1
print(int(ret)) # c++에서 그대로 옮기면서 실수가 있었던 부분 (파이썬은 정수타입 강제가 없어므로 int 처리 필수)

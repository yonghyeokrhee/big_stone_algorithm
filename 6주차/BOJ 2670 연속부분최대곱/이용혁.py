import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(float(input().rstrip()))

dp = [0] * n
dp[0] = arr[0]
for i in range(1,n):
    dp[i] = max(dp[i-1], 1) * arr[i]
print(dp)
print('%.3f' % max(dp))
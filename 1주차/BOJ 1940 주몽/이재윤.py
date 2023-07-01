// 시간 복잡도를 고려하여 1차원 for문으로 풀어야 한다

N = int(input())
M = int(input())

arr = list(map(int, input().split()))
ans = 0
memo = []

for i in range(0, len(arr)):
   
   num = arr[i]
   
   if M-num in memo:
       ans += 1

   memo.append(num)
   

print(ans)

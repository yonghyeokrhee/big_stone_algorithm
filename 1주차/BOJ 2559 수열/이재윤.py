// maxSum을 적절하게 초기화해줘야 한다
// 시간 복잡도를 고려해서 투 포인터 방식으로 풀어야 한다 

N, K = map(int, input().split())
arr = [] 
maxSum = -99999999 

arr = list(map(int, input().split()))
sum = 0     
    
for i in range(0, K):
    sum += arr[i]
    
maxSum = max(maxSum, sum)
    
    
for i in range(K, N):
    sum += arr[i]
    sum -= arr[i-K]
    maxSum = max(maxSum, sum)

print(maxSum)

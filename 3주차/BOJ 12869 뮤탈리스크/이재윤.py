// 다시 한 번 정리해보자

N= int(input())

dp = [[[0 for _ in range(61)] for _ in range(61)] for _ in range(61)]

ans = 0

def dfs(a, b, c):
    

    if a == 0 and b == 0 and c == 0:
        return 0
        
    if dp[a][b][c]:
        return dp[a][b][c]
  
    
    dp[a][b][c] = 1 + min(dfs(max(0, a-9), max(0, b-3), max(0, c-1)), dfs(max(0, a-9), max(0, b-1), max(0, c-3)), dfs(max(0, a-3), max(0, b-9), max(0, c-1)), 
                          dfs(max(0, a-3), max(0, b-1), max(0, c-9)), dfs(max(0, a-1), max(0, b-9), max(0, c-3)), dfs(max(0, a-1), max(0, b-3), max(0, c-9)))
                          
    
    return dp[a][b][c]

    
    

scv = list(map(int, input().split()))
while len(scv) < 3:
    scv.append(0)
  
  
ans = dfs(scv[0], scv[1], scv[2])
    
print(ans)


    
    







        

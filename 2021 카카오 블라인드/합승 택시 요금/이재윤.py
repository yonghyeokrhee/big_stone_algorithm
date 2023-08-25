def floyd_warshall(n, cost):
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i == j:
                    cost[i][j] = 0
                else:
                    cost[i][j] = min(cost[i][k]+cost[k][j], cost[i][j])
                    

def solution(n, s, a, b, fares):   
    INF = int(1e9)
    ans = INF

    cost = [[INF]*(n+1) for _ in range(n+1)]
    
    for i, j, c in fares:
        cost[i][j] = c
        cost[j][i] = c 
        
    floyd_warshall(n, cost)
    
    for i in range(1, n+1):
        ans = min(ans, cost[s][i]+cost[i][a]+cost[i][b])
        
    
    return ans

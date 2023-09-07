def solution(n, s, a, b, fares):
    answer = 0
    
    INF = int(1e9)
    
    cost = [[INF]*(n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                cost[i][j] = 0 
    
    for fare in fares:
        start, end, c = fare[0], fare[1], fare[2]
        cost[start][end] = min(cost[start][end], c)
        cost[end][start] = min(cost[end][start], c)
        
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                cost[i][j] = min(cost[i][j], cost[i][k]+cost[k][j])
                
    minCost = cost[s][a] + cost[s][b] 
    for i in range(1, n+1):
        if i != s:
            minCost = min(minCost, cost[s][i]+cost[i][a]+cost[i][b])
            
    answer = minCost        
    
    return answer

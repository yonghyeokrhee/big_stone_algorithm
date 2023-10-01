from collections import deque


K = int(input())


def bfs(start, edge, visited):
    
    
    q = deque()
    q.append((start, 1))
    
    visited[start] = 1
    
    
    while q:
        
        num, color = q.popleft()
        
        
        for next in edge[num]:
            if visited[next] == 0:
                if color == 1:
                    visited[next] = 2
                    q.append((next, 2))
                else:
                    visited[next] = 1
                    q.append((next, 1))
            else:
                if color == 1:
                    if visited[next] == 2:
                        continue
                    else:
                        return False
                if color == 2:
                    if visited[next] == 1:
                        continue
                    else:
                        return False
    
    
    
    return True 
    
    



for i in range(K):
    
    V, E = map(int, input().split())
    edge = [[] for _ in range(V+1)]
    
    for j in range(E):
        u, v = map(int, input().split())
        edge[u].append(v)
        edge[v].append(u)
        
        
    visited = [0]*(V+1)
    
    ans = "YES"
    
    for j in range(1, V+1):
        if visited[j] == 0:
            res = bfs(j, edge, visited)
            if res == False:
                ans = "NO"
                
    print(ans)
  

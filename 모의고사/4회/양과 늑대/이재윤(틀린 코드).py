

sheepCnt = 0
wolfCnt = 0 


def dfs(pos, info, graph, visited):
    
    global sheepCnt
    global wolfCnt 
    
    
    if visited[pos] == False:
        if info[pos] == 0:
            sheepCnt += 1 
        else:
            wolfCnt += 1 
        
        visited[pos] = True 
            
    visitCnt = 0             
    
    for next in graph[pos]:
        if visited[next] == False:
            if info[next] == 0:
                visitCnt += 1 
                dfs(next, info, graph, visited)
            elif info[next] == 1 and sheepCnt - wolfCnt >= 2:
                visitCnt += 1 
                dfs(next, info, graph, visited)
            
            
    if visitCnt == 0 and info[pos] == 1:
        visited[pos] = False
        wolfCnt -= 1 
        return 
    
    
    for next in graph[pos]:
        if visited[next] == False:
            if info[next] == 0:
                visitCnt += 1 
                dfs(next, info, graph, visited)
            elif info[next] == 1 and sheepCnt - wolfCnt >= 2:
                visitCnt += 1 
                dfs(next, info, graph, visited)
                
             
    if visitCnt == 0 and info[pos] == 1:
        wolfCnt -= 1 
        return 
    
    
    
  
def solution(info, edges):
    answer = 0
    
    visited = [False]*len(info)
    graph = [[] for _ in range(len(info))]
    
    for edge in edges:
        a = edge[0]
        b = edge[1]
        
        graph[a].append(b)
    
    
    dfs(0, info, graph, visited)
    
    answer = sheepCnt 
    

    
    
    
    return answer

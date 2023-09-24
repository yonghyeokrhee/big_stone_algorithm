import sys
sys.setrecursionlimit(2506)
def solution(n, m, x, y, r, c, k):
    if (k - (abs(x-r) + abs(y-c))) % 2:
        return "impossible"
    if k < (abs(x-r) + abs(y-c)):
        return "impossible"
    dist = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            dist[i][j] = abs(j-c+1) + abs(i-r+1)
    
    dx = [1,0,0,-1]
    dy = [0,-1,1,0]
    dict = {0:'d',1:'l',2:'r',3:'u'} # debugging 용
    answer  = []
    def dfs(x,y,r,c,k):
        # 만약 남은 거리가 남은 k와 같다면 종점으로 돌아오기 위해 멈춘다. 
        if x==r and y==c and k==0:
            return
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
        
            if nx<=0 or nx > n or  ny<=0 or ny > m:
                continue
            elif dist[x-1][y-1] < k:
                answer.append(dict[i])
                return dfs(nx,ny,r,c, k-1)
            elif dist[x-1][y-1] == k and dist[nx-1][ny-1] == k-1:
                answer.append(dict[i])
                return dfs(nx,ny,r,c, k-1)

               
    dfs(x,y,r,c,k)

    return ''.join(answer)

#print(solution(3,4,2,3,3,1,5))
print(solution(10,10,1,1,10,10,18))
print(solution(10,10,1,1,10,10,4))
import sys
sys.setrecursionlimit(2500)
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
    def dfs(x,y, k):
        # 만약 남은 거리가 남은 k와 같다면 종점으로 돌아오기 위해 멈춘다. 
        if dist[x-1][y-1] == k:
            print("돌아온다")
            return x, y, k
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 < nx <= n and 0 < ny <= m:
                answer.append(dict[i])
                return dfs( nx,ny, k-1)
    final_x, final_y , final_distance = dfs(x,y,k)
    print(final_x,final_y,final_distance)

    def dfs_2(x,y,r,c,k): # 만약 남은거리가 k와 같다면 우선순위에 따라서 돌아온다. d,l,r,u
        if x==r and y==c:
            return print("도착")
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 < nx <= n and 0 < ny <= m and k-1 == dist[nx-1][ny-1]:
                answer.append(dict[i])
                return dfs_2(nx,ny,r,c,k-1)

    dfs_2(final_x,final_y,r,c,final_distance)

    return ''.join(answer)
#print(solution(3,4,2,3,3,1,5))
print(solution(10,10,1,1,10,10,18))
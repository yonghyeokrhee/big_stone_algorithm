import sys
sys.setrecursionlimit(10000)


def DFS(x,y):
    
    dy = [0,1,0,-1]
    dx = [-1,0,1,0]
    
    visited[y][x] = 1
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if (nx < 0) or (ny < 0) or (nx >= M) or (ny >= N):
            continue
        elif (a[ny][nx]==1) and (not visited[ny][nx]):
            DFS(nx,ny)
    return 0
            
T = int(input()) # test case 개수

for _ in range(T):
    
    M, N, K = map(int, input().split())
    
    a = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        a[y][x] = 1
   
    ret = 0
    for i in range(N):
        for j in range(M):
            if a[i][j] == 1 and not visited[i][j]:
                ret += 1
                DFS(j, i)
    print(ret)

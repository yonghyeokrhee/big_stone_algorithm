K = int(input())
arr = [[*map(int,input().split())] for _ in range(K)]

visited = [[0]*101 for _ in range(101)]
# 드래곤 커브
dx = [1,0,-1,0]
dy = [0,-1,0,1]

for ar in arr:
    x,y,d,g = ar
    cum_rots = [d]
    new_rots = [d]
    visited[y][x] = 1
    flag = False
    for i in range(g+1):
        for r in new_rots:
            nx = x + dx[r]
            ny = y + dy[r]
            if nx > 100 or ny > 100:
                flag = True
                break
            else:
                visited[ny][nx] = 1
                x ,y = nx, ny
        if flag:
            break
        else:
            new_rots = [(j + 1) % 4 for j in cum_rots[::-1][:]]
            cum_rots += new_rots

cnt = 0
for k in range(100):
    for j in range(100):
        if all([visited[k][j], visited[k+1][j],visited[k][j+1],visited[k+1][j+1]]):
            cnt += 1
print(cnt)


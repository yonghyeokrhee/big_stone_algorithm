from collections import deque
N, M = map(int , input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

x, y = 0, 0

# 좌우상하
v = [-1, 1,0,0]
h = [0,0,-1, 1]

visited = [[0]* M for _ in range(N)]

# 탐색을 시작한 곳을 먼저 박아준다.
visited[y][x] = 1

# Queue를 관리하는 것 시작. (처음에만 필요한 것)
q = deque()

q.append((y,x))
# Queue가 모두 소진될때까지 한다.
while q:
    here = q.popleft() # 이번 round에서 시작하는 곳
    # 시작한 곳은 우선 방문한것으로 보자.
    if here == (N-1,M-1): # 종료조건
        break
    else:
        for i in range(4): # 상하 좌우 살피기 -> 이게 끝난 후에 적절한 좌표들은 Queue에 들어가 있어야 한다.
        # 적절한 좌표라 함은 1의 값을 가진 곳들이 Queue에 들어가야 한다는 뜻이다. 
        # visited를 잘 기록해두어야지 이미 시작한 곳으로 돌아가지 않는다. here는 곳 visited이다. 
            ny = here[0] + v[i]
            nx = here[1] + h[i]
            if (nx <0) or (nx>M-1) or (ny>N-1) or (ny < 0) or (graph[ny][nx] == 0) or visited[ny][nx]: # 말 안되는 조건들 빼주기 # 최소거리 구하려면 돌아가면 안됨. # 0인 곳은 방문할 필요도 없음
                continue
    
            elif graph[ny][nx] == 1:
                q.append((ny,nx)) # 내가 방문해야 하는 곳은 queue에 추가해두자.
                visited[ny][nx] += visited[here[0]][here[1]] + 1 # 갈 길을 미리 visited 로 기록을 해두자.

   
print(visited[N-1][M-1])

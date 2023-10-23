from collections import deque
def solution(board):
    # for b in board:
    #     print(b)
    #[코너개수][y좌표][x좌표][수평수직]
    v = [[[[0]*2 for _ in range(len(board))] for _ in range(len(board))] for _ in range(len(board)**2+1)] # 코너의 상태(개수)에 대하여 가장 먼저 접근한다.
    dy = [1,0,-1,0]
    dx = [0,1,0,-1]
    hvs = [1,0,1,0] # 1은 수직, 0은 수평이동
    # 코너의 개수를 추가적인 상태값으로 하여 BFS를 만들 수 있을까? 코너의 기록, 현재 방향과 다음 방향이 꺽어질 때 코너라고 한다.
    def bfs()->int:
        q = deque()
        q.extend([[0,0,0,0,[]],[0,0,0,1,[]]]) # 처음 시작은 오른쪽으로 아래로 두군데로 갈 수 있기 때문에 두 개의 queue로 시작한다.
        v[0][0][0][0] = 1
        v[0][0][0][1] = 1
        #todo: 거리를 제대로 기록하기 위해서는 bfs의 level이 맞는지 확인해봐야 한다.
        #todo: 자신이 방문했던 곳을 다시 방문하지 않으려면 cost를 기준으로 판단하거나(cost가 더 낮다면 포기), bfs 경로에 따라서 자신이 방문한 곳을 기록 하지 않도록 위치 정보를 기록해두어야 한다. 두 번째가 더 낫다.
        while q:
            corner, y,x,hv, visit = q.popleft()
            for i in range(4):
                # 수평 i = 1,2 , 수직 i = 0,3
                ny = y + dy[i]
                nx = x + dx[i]
                new_corner = corner + 1 if hv != hvs[i] else corner
                if ny < 0 or nx < 0 or ny >=len(board) or nx >= len(board) or v[new_corner][ny][nx][hvs[i]] or board[ny][nx]:
                    continue
                if (ny,nx) in visit: # 자신의 이동 경로상 방문한적이 있다면 진행하지 않는다.
                    continue
                q.append([new_corner, ny,nx,hvs[i], visit+[(ny,nx)]])
                v[new_corner][ny][nx][hvs[i]] = v[corner][y][x][hv] + 1 # 한칸 이동했으니까 거리를 더해줌.
        return v # 도착점 기준 누적 거리
    answer = bfs()

    cost = 10e+9
    for corner in range(len(v)):
        for i in range(2):
            if v[corner][len(board) - 1][len(board) - 1][i] == 0:
                continue
            dist = v[corner][len(board) - 1][len(board) - 1][i] - 1  # 코너 수는 같은 두 가지 도착 방향에 대하여 모두 계산 해본다.
            cost = min(cost, dist * 100 + corner * 500)
    return cost

#print(solution([[0,0,0],[0,0,0],[0,0,0]])) # 코너는 한개 밖에 나올 수가 없다.

print(solution(	[[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]))
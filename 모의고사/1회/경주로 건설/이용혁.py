from collections import deque
def solution(board):
    #[코너개수][y좌표][x좌표][수평수직]
    v = [[[[0]*2 for _ in range(len(board))] for _ in range(len(board))] for _ in range(len(board)**2+1)] # 코너의 상태(개수)에 대하여 가장 먼저 접근한다.
    dy = [1,0,-1,0]
    dx = [0,1,0,-1]
    hvs = [1,0,1,0] # 1은 수직, 0은 수평이동
    def bfs()->int:
        q = deque()
        q.extend([[0,0,0,0,[]],[0,0,0,1,[]]]) # 처음 시작은 오른쪽으로 아래로 두군데로 갈 수 있기 때문에 두 개의 queue로 시작한다.
        v[0][0][0][0] = 1
        v[0][0][0][1] = 1
        while q:
            corner, y,x,hv, visit = q.popleft()
            for i in range(4):
                # 수평 i = 1,3 , 수직 i = 0,2
                ny = y + dy[i]
                nx = x + dx[i]
                new_corner = corner + 1 if hv != hvs[i] else corner
                if ny < 0 or nx < 0 or ny >=len(board) or nx >= len(board) or v[new_corner][ny][nx][hvs[i]] or board[ny][nx]:
                    continue
                if (ny,nx) in visit:
                    continue
                q.append([new_corner, ny,nx,hvs[i], visit+[(ny,nx)]])
                v[new_corner][ny][nx][hvs[i]] = v[corner][y][x][hv] + 1 # 한칸 이동했으니까 거리를 더해줌.
        return v
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
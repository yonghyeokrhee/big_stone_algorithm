from collections import deque
def solution(board):
    for b in board:
        print(b)
    #[코너개수][y좌표][x좌표][수평수직]
    v = [[[[0]*2 for _ in range(len(board))] for _ in range(len(board))] for _ in range(len(board)**2+1)] # 코너의 상태(개수)에 대하여 가장 먼저 접근한다.
    dy = [1,0,-1,0]
    dx = [0,1,0,-1]
    hvs = [1,0,0,1] # 1은 수직, 0은 수평이동
    # 코너의 개수를 추가적인 상태값으로 하여 BFS를 만들 수 있을까? 코너의 기록, 현재 방향과 다음 방향이 꺽어질 때 코너라고 한다.
    def bfs()->int:
        q = deque()
        q.extend([[0,0,0,0],[0,0,0,1]]) # 처음 시작은 오른쪽으로 아래로 두군데로 갈 수 있기 때문에 두 개의 queue로 시작한다.
        v[0][0][0][0] = 1
        v[0][0][0][1] = 1
        while q:
            corner, y,x,hv = q.popleft()
            for i in range(4):
                # 수평 i = 1,2 , 수직 i = 0,3
                ny = y + dy[i]
                nx = x + dx[i]
                new_corner = corner + 1 if hv != hvs[i] else corner
                if ny < 0 or nx < 0 or ny >=len(board) or nx >= len(board) or v[new_corner][ny][nx][hvs[i]] or board[ny][nx]:
                    continue
                q.append([new_corner, ny,nx,hvs[i]])
                print(f"number of corner is: ", new_corner)
                print(f"moving to {ny},{nx}")
                v[new_corner][ny][nx][hvs[i]] = v[corner][y][x][hv] + 1 # 한칸 이동했으니까 거리를 더해줌.
        return v[len(board)-1][len(board)-1] -1 # 도착점 기준 누적 거리
    answer = bfs()
    return answer * 100 # 모든 거리가 100원의 비용이 든다고 하면?

print(solution([[0,0],[0,0]])) # 코너는 한개 밖에 나올 수가 없다.

#print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
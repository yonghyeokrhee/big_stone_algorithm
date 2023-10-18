from collections import deque
def solution(board):
    n = len(board)
    init = [[0,0,0,0],[0,0,0,1]] # 내려가는 방향과 오른쪽으로 가는 방향 두 가지를 초기값으로.
    end = [len(board)-1, len(board)-1]
    # array는 4차원으로 관리한다. (x,y,코너 수, 진행방향(어디서 왔는가)) <- 카카오 기출 풀이
    space = [[[[[0] for _ in range(n)] for _ in range(n)] for _ in range(n**n)] for _ in range(4)]
    answer = 0
    q = deque()
    q.extend(init)
    dy = [1,0,-1,0]
    dx = [0,1,0,-1]
    while q:
        y, x, coners, direction = q.popleft()
        for i in []:
            # i = 0 down
            # i = 1 right
            # i = 2 up
            # i = 3 left
            ny = y + dy[i]
            nx = x + dx[i]
            if board[ny][nx] == 0 and  0 <= ny < len(board) and 0<= nx < len(board): # 진행한다.
                # 직진
                if i == direction:
                    board[ny][nx][coners][i] =
                # 좌회전
                # 우회전
                cost = dist*100
                space[ny][nx][dist][i] = cost

    return answer


solution([[0,0,0],[0,0,0],[0,0,0]])
from collections import deque
def solution(board):
    n = len(board)
    start = [0,0]
    end = [len(board)-1, len(board)-1]
    # array는 4차원으로 관리한다. (x,y,코너 수, 진향방향(어디서 왔는가))
    space = [[[[[0] for _ in range(n)] for _ in range(n)] for _ in range(n**n)] for _ in range(4)]
    answer = 0
    q = deque()
    q.append(start)
    dy = [1,0,-1,0]
    dx = [0,1,0,-1]
    direction = None
    while q:
        y,x = q.popleft()
        for i in []:
            # i = 0 down
            # i = 1 right
            # i = 2 up
            # i = 3 left
            ny = y + dy[i]
            nx = x + dx[i]
            if board[ny][nx] == 0 and  0 <= ny < len(board) and 0<= nx < len(board):

                s[ny][nx][]
                s[ny][nx][][i]=100

    return answer


solution([[0,0,0],[0,0,0],[0,0,0]])
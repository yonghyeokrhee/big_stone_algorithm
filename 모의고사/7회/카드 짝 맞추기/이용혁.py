import sys
sys.setrecursionlimit(10000)
def solution(board, r, c):
    global mn
    global recursion
    mn = 100000000
    recursion = 0

    def check(board) -> int:
        """
        unique한 카드 짝 개수를 기록한다. dfs의 종료조건에 사용한다.
        :return: 카드짝의 unique한 경우의 수
        """
        u_pair = set()
        for j in range(4):
            for i in range(4):
                if board[j][i] > 0:
                    u_pair.add(board[j][i])
        return len(u_pair)

    v = [[0]*4 for _ in range(4)] # 초기 값.
    def dfs(r,c,n,cnt,target:tuple,mode)->int:
        print("target is: ", target)
        global mn
        global recursion
        """
        움직임의 종료는 모두 8가지 상하좌우,ctrl 상하좌우이며 dfs로 같은 숫자를 만나면 작동횟수를 기록한다.
        모든 카드 짝을 다 없애면 종료한다.
        """

        v[r][c] = 1
        recursion+=1

        if board[r][c] > 0:
            #print(f"Program opened the card at ({r}),({c})")
            if mode and board[target[0]][target[1]] == board[r][c] and target[0]!=r and target[1]!=c:
                print(f"target eliminated at ({r}),({c})")
                print(f"target was : {target[0]},{target[1]}" )
                n -= 1 # True 인 상태에서 pair를 찾았다면 n을 감소시킨다.
                board[target[0]][target[1]] = 0 # target을 복원한다.
                board[r][c]=0 # 두 번째 board 값을 0으로 복원한다.
                board[target[0]][target[1]] = 0 # 첫 번째 board 값도 0으로 변경
                for j in range(4): # visit 행렬 복원시키기.
                    for i in range(4):
                        v[j][i]=0
                target = [r,c] #target 복원
                print("initiated")
                print("n:",n)
                print("recursion: ",recursion)
            else:
                target = [r,c] # 숫자를 만나면 target을 설정한다.
            mode = not mode
            cnt += 1 # enter를 해야하기 때문에 올려준다.
            # print(f"this time target is: ", target)
            # print(f"counting:", cnt)
            # print(f"pair to left ", n)

        if n == 0:# 모든 카드를 다 뒤집었다면 종료한다.
            print("program terminated!!")
            for b in board:
                print(b)
            mn = min(cnt,mn) # 전역 변수로 처리한다.
            return
        # 8가지 이동이 있음.
        dc = [1,-1,0,0]
        dr = [0,0,-1,1]
        # 상하좌우는 단순하다.
        for i in range(4):
            nc = c + dc[i]
            nr = r + dr[i]

            if nr < 0 or nr >=4 or nc < 0 or nc >=4 or v[nr][nc]:
     #           print(f"nr,nc: {nr},{nc}")
                continue
            dfs(nr, nc, n, cnt+1, target, mode)
            for j in range(4):  # visit 행렬 복원시키기.
                for i in range(4):
                    v[j][i] = 0
            # dfs(r,c+1) # 좌
            # dfs(r,c-1) # 우
            # dfs(r-1, c) # 상
            # dfs(r+1, c) # 하
        # control 연산
        # dfs()
        # dfs()
        # dfs()
        # dfs()
        return # 정상적이라면 n이 0이 되면서 종료되므로 필요 없다. 비정상인 경우 for 문 다 돌았을 때 종료 (debug용)

    n = check(board)
    dfs(r,c,n,0,[r,c],False)

    return mn

print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],1,3))
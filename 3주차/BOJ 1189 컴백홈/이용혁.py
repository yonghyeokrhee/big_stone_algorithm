
R, C, K = map(int,input().split())
arr = [list(input()) for _ in range(R)]


dx = [1,-1,0,0]
dy = [0,0,-1,1]

v = [[0]*C for _ in range(R)]

def erase(x,y):
    # 되돌리기
    global dist
    v[y][x] = 0
    dist -= 1

def check(nx, ny):
    # T가 아니고 이전에 방문했던 곳이 아니라면
    if (nx >= C) or (ny >= R) or (ny < 0) or (nx < 0) or (arr[ny][nx]) == 'T' or (v[ny][nx]):
        return False
    else:
        return True

def go(x,y):
    global dist
    global ret
    # 일단 시작할 때 거리를 1로 본다.
    dist += 1 # 들어올 떄 마다 하나씩 더해주기. 
    # base case
    if x == C-1 and y == 0:  # 종료 조건을 충족한다면
        print(dist)
        if dist == K: # 만약 K 거리라면
            ret += 1 # 정답 cnt
            print("return : ", ret)

        return # 함수를 종료 시킨다.
    # 전후 좌우를 살피고
    # 만약 T가 아니라면 check 함수로 확인하기
    for i in range(4): # 이동하기
        ny= y + dy[i]
        nx = x + dx[i]
        if check(nx, ny):
            v[ny][nx] = 1 # 방문 사실을 기록한뒤
            go(nx,ny) # 계속 들어간다.
            erase(nx,ny)#원복 코드
            print(f"going ({nx}), ({ny})")



#시작점은 하나다.
#종료조건도 같다.
dist = 0
ret = 0
v[R-1][0] = 1
go(0,R-1) # 왼쪽 아래에서 한번만 시작하면 됨.

print(ret)

#완탐과 원복
    # dfs 인데 끝까지 도착하면 종료하고 거리를 기록한다.
    #하나를 끝까지 탐색했으면 한 leaf를 올라오는 원복을 시켜주고 (visited를 삭제해주고) 다시 dfs를 내려간다.
    # 계속 반복한다.

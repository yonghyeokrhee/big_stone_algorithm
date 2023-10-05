n = int(input())
arr = [[0]*n for _ in range(n)]
v = [[0]*n for _ in range(n)]
#n개의 queen 놓기

# dfs(0) -> dfs(1) -> dfs(2) -> dfs(3) -> ... 이렇게 진행하다가 n이 도달하면 종료하고 return 한다.
# 도달하지 못하고 끝나면 종료조건을 만나지 못하므로 정답을 반환할 수 없다.
cnt = 0
loc = []

def cross_check(a,b):
    """
    대각선 공격이 가능한지 확인할 수 있는 함수
    :return: True or False
    """
    for l in loc: # 앞서 존재하는 모든 loc 에 대하여...
        if abs(a-l[0])  == abs(b-l[1]):
            return False
    return True

def dfs(col,q):
    global cnt
    if q == 0:  # queen을 모두 놓았다면 count를 더해주고 종료한다.
        cnt += 1
        # print(loc)
        return
    for i in range(len(col)):
        if col[i]:
            continue
        if cross_check(len(col)-q,i): # 앞서 모든 loc 들과의 충돌이 없다면 queen을 놓을 수 있다.
            # print("safe to put")
            col[i]=True # queen 놓기
            loc.append([len(col)-q, i]) # 가장 처음에 놓는 곳은 (0,0)
            dfs(col, q-1)
            col[i]=False
            loc.pop() # 놓았던 것 빼기

         # queen을 놓을 수 없다면 종료한다.
dfs([False]*n, n)
print(cnt)
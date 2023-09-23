import sys
sys.setrecursionlimit(10**6)
def solution(n, m, x, y, r, c, k):

    s = (x,y)
    e = (r,c)
    answer_arr = []
    dy = [1,0,0,-1]
    dx = [0,-1,1,0]
    dict = {0:'d',1:'l',2:'r',3:'u'}
    answer = []
    def dfs(loc,cnt):
        if answer:
            return
        if cnt == k:
            # print(answer_arr)
            # print(loc)
            if loc == e:
                # print("arrive")
                answer.append(answer_arr[:])
                return
            else:
                return
        # 가장 빠른 문자열을 무조건 선택한다.
        for i in range(4):
            ny = loc[0] + dy[i]
            nx = loc[1] + dx[i]
            if 0< ny <= n and 0< nx <= m:
                answer_arr.append(i)
                cnt += 1
                loc = (ny, nx)
                dfs(loc,cnt)
                cnt -= 1
                answer_arr.pop()
    dfs(s,0)
    return ''.join([dict[i] for i in answer[0]]) if answer else 'impossible'
print(solution(3,4,2,3,3,1,5))
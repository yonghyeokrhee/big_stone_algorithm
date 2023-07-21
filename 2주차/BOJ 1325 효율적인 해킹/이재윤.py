// 많이 배운 문제
// pypy3로 채점해야 하고, bfs로 하는 편이 좋다
// N이 10000임을 고려해서, 시간 초과에 주의 해야 한다
// 2차원 리스트에 넣는 법을 알아야 한다
// from collections import deque 즉, 큐 사용에 익숙해져야 한다

from collections import deque

N, M = map(int, input().split())

trust = [[] for _ in range(N+1)]
ans = [0]*(N+1)
maxCnt = -int(1e9)
cnt = 0 

for i in range(M):
    a, b = map(int, input().split())
    trust[b].append(a)
    
def bfs(num):

    visited = [False]*(N+1)
    visited[num] = True
    q = deque()
    q.append(num)
    global cnt
    cnt += 1 
    
    while q:
        num = q.popleft()
    
        for next in trust[num]:
            if visited[next] == False:
                visited[next] = True 
                cnt += 1 
                q.append(next)
    
    
for i in range(1, N+1):
    cnt = 0 
    bfs(i)
    maxCnt = max(maxCnt, cnt)
    ans[i] = cnt 
    
for i in range(1, N+1):
    if ans[i] == maxCnt:
        print(i, end=' ')

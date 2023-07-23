# Y, X = 13, 12
#
# cheese = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
#     [0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
#     [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
#     [0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0],
#     [0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0],
#     [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
#     [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
#     [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
#     [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
#     [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# ]

# Y, X = 5, 5
# cheese =\
# [[0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0],
# [0, 0, 1, 0, 0],
# [0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0]]


Y, X = 10, 12
cheese = \
[[0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0, 0],
[0, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 0],
[0, 1, 1 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,1, 0],
[0, 1, 0 ,1 ,0 ,1 ,0 ,1 ,1 ,0 ,1, 0],
[0, 1, 0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0, 0],
[0, 1, 0 ,1 ,0 ,0 ,1 ,1 ,1 ,0 ,1, 0],
[0, 1, 0 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1, 0],
[0, 1, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1, 0],
[0, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 0],
[0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0, 0]]

for c in cheese:
    print(c)


from collections import deque

queue = deque()

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

y,x = 0,0
def BFS(cheese):
    queue.append((y, x))
    airs = [[0] * X for _ in range(Y)]
    visited = [[0] * X for _ in range(Y)]
    visited[y][x] = 1
    while queue:
        here = queue.popleft()
        for i in range(4):
            ny = here[0] + dy[i]
            nx = here[1] + dx[i]
            if (nx < 0) or (nx > X - 1) or (ny > Y - 1) or (ny < 0) or (cheese[ny][nx] == 1) or visited[ny][nx]:  # 말 안되는 조건들 빼주기 # 최소거리 구하려면 돌아가면 안됨. # 0인 곳은 방문할 필요도 없음
                continue
            #print("going :", (ny,nx))
            if cheese[ny][nx] == 0 and not visited[ny][nx]:
                airs[ny][nx] = "a"  # 공기라고 표시
                queue.append((ny,nx)) # 큐에 넣어두기
                visited[ny][nx] = 1
    return airs
loop = 0
melted = []
flag = True
while flag:
    airs = BFS(cheese)
    s = set()
    visited = [[0] * X for _ in range(Y)]
    for j in range(Y-1):
        for i in range(X-1):
            if cheese[j][i]==1:
                for k in range(4):
                    ny = j + dy[k]
                    nx = i + dx[k]
                    if airs[ny][nx] == 'a' and not visited[ny][nx]:
                        s.add((j,i))
    melted.append(len(s))
    flag = len(s)
    # print(sorted(s))
    # print("previsous colelction is: ", len(s))
    # 녹이기 변환
    for t in s:
        cheese[t[0]][t[1]] = 0
    # for c in cheese:
    #     print(c)
    loop += 1
print(loop-1)
print(melted[-2])
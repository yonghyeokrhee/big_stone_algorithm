from collections import deque


def solution(places):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    answer = [True] * 5
    for ind, p in enumerate(places):
        p = [*map(list, p)]
        for i in range(5):
            for j in range(5):
                q = deque()
                if p[i][j] == "P":
                    q.append((i, j))
                    v = [[0] * 5 for _ in range(5)]
                    v[i][j] = 1
                    d = 0
                    while q and answer[ind] and d < 2:
                        y, x = q.popleft()
                        for i in range(4):
                            ny = y + dy[i]
                            nx = x + dx[i]
                            if (
                                ny >= 5
                                or nx >= 5
                                or ny < 0
                                or nx < 0
                                or v[ny][nx]
                            ):
                                continue
                            elif p[y][x] =='O' and p[ny][nx] == "P":
                                answer[ind] = False
                                break
                            else:
                                v[ny][nx] == 1
                                if p[ny][nx] == 'O':
                                    q.append((ny, nx))
                        d += 1
    return list(map(int,answer))

tc = [
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
]
print(solution(tc))

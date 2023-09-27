from collections import defaultdict

cnt_lamb = 0
cnt_wolf = 0
visit = [0] * 18

def solution(info, edges):
    d = defaultdict(list)
    for e in edges:
        d[e[0]].append(e[1])

    def dfs(node):
        global cnt_lamb, cnt_wolf
        if info[node] and not visit[node]:
            cnt_wolf += 1
        elif not info[node] and not visit[node]:
            cnt_lamb += 1
        visit[node] = True

        if not d[node]:
            return
        for there in sorted(d[node],
                            key=lambda x: info[x]):  # 0부터 정렬해서 양이 있는 것부터..

            if cnt_wolf + info[there] >= cnt_lamb:
                continue
            dfs(there)
            if info[there]:
                cnt_wolf -= 1

    flag = True
    while flag:
        prev = cnt_lamb
        dfs(0)
        post = cnt_lamb
        flag = max(post - prev, 0)

    return cnt_lamb
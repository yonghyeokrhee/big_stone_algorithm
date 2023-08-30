from collections import deque
from collections import defaultdict


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if len(edges) == 0:
            return [0]
        d = defaultdict(list)
        mn = 1000000000
        # 양방향 간선 그래프
        mx = 0
        for i in edges:
            d[i[0]].append(i[1])
            d[i[1]].append(i[0])
            mx = max(mx, i[0], i[1])

        answer = defaultdict(list)
        for root in range(mx + 1):
            depth = 0
            q = deque()
            v = [0] * 2 * 10000
            q.append(root)
            while q:
                w = len(q)
                for _ in range(w):
                    node = q.popleft()
                    v[node] = True
                    for n in d[node]:
                        if not v[n]:
                            q.append(n)
                depth += 1  # 다 돌았으므로 depth 추가
            depth -= 1
            if depth <= mn:
                answer[depth].append(root)
                mn = depth

        return answer[mn]
class Nodes:
    def __init__(self):

        self.val
        self.left
        self.right

def solution(nodeinfo):
    nodes = sorted(nodeinfo,key=lambda x : (-x[1],x[0]))

    def dfs(root):
        nodes.remove(root)
        if root[0] < nodes[0][0] and root[1] > nodes[0][1]:

            dfs(nodes[0])

    dfs(nodes[0])
    answer = [[]]
    return answer


solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]])
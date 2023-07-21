
mydict = [[0] * 3 for _ in range(3)]
mydict[0][1] = 1
mydict[0][2] = 1
visited = [0,0,0]
def DFS(x):
    ret = 1
    for loc in range(len(mydict[x])):
        ret += mydict[x][loc]
    return ret

print(DFS(0))

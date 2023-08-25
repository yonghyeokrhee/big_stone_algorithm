import numpy as np

def htransform(arr,r,c):
    # 가로 변환
    answer = [[] for _ in range(r)]
    for i in range(r):
        for j in range(0,c,2):
            answer[i].append(max(arr[i][j],arr[i][j+1]))

    return answer

def vtransform(arr,r,c):
    # 세로변환
    answer = [[] for _ in range(int(r/2))]
    for i in range(0,r,2):
        for j in range(c):
            answer[int(i/2)].append(min(arr[i][j], arr[i+1][j]))

    return answer

def solution(arr,k):

    if k == 0: # transform을 종료한다.
        return arr

    r,c = len(arr), len(arr[0])

    if c >= r: # 가로가 세로보다 길거나 같으면
        arr = htransform(arr,r,c)
    else:
        arr = vtransform(arr,r,c) # 아니면 세로변환

    return solution(arr,k-1)



#ret = solution([[5, 4, 8, 7], [7, 3, 1, 2], [3, 8, 12, 6], [11, 4, 5, 4]], 4)
#ret = solution([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14],[15,16]],2)
ret = solution([[1],[2]],2)
print(ret)
// start, end, mid라는 변수들을 활용한다
// 이차원 list를 만들어서 거기에 값을 저장한 후에 출력한다 

import math 

K = int(input())

arr = list(map(int, input().split()))

total = math.pow(2, K)-1 
ans = [[] for _ in range(K+1)]


def dfs(start, end, height):
    
    mid = int((start+end) // 2) 
    ans[height].append(arr[mid])
    
    if start == end:
        return 
    
    dfs(start, mid-1, height+1)
    dfs(mid+1, end, height+1)
    
    
    
dfs(0, total-1, 1)

for i in range(1, K+1):
    for j in range(len(ans[i])):
        print(ans[i][j], end=' ')
    print('', end='\n')



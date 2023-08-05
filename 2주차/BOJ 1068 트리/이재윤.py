// root가 항상 0이 아닐 수 있음을 주의해야 한다
// 문제에 어디에도 root가 항상 0이라는 답이 존재하지 않는다
// 이 점을 고려해야 한다 
// ret로 리프 노드의 합을 구하는 코드가 매우 유용할듯 하다
// 이 점을 잘 활용해보도록 한다
// 그리고 visited를 굳이 쓰지 않아도 괜찮다   

N = int(input())
parent = list(map(int, input().split()))

arr = [[] for _ in range(N)]
ans = 0
root = 0 

for i in range(N):
    num = parent[i]
    if num == -1: 
        root = i 
        continue
    arr[num].append(i)


r = int(input())


def dfs(num):
    
    ret = 0 
    child = 0 
    
    for next in arr[num]:
        if r == next:
            continue
        ret += dfs(next)
        child += 1     
    
    if child == 0:
        return 1 
        
    return ret 



if root == r:
    print(0)
else:
    print(dfs(root))


    
    
    

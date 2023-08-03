// q로 만들어서 푼다는 아이디어, rCnt를 세서, 그것이 짝수일 때와 홀수일 때 q의 각각 앞 뒤에서 빼준다는 것 
// 이 두 가지 아이디어가 중요하다 
// flag를 활용한 점도 중요하다 

from collections import deque 
T = int(input())

for i in range(T):
    
    p = input()
    
    n = int(input())
    
    arr = input()
    arrList = arr[1:len(arr)-1].split(",")
    q = deque(arrList)
    flag = 0 
    
    if n == 0:
        q = [] 
    
    rCnt = 0
    dCnt = 0 
    
    for c in p:
        if c == 'R':
            rCnt += 1 
        elif c == 'D':    
            if len(q) == 0:
                flag = 1 
                print("error")
                break
    
            if rCnt % 2 == 0:
                q.popleft()
            else:
                q.pop()
    if flag == 0:
        if rCnt % 2 == 0:
            print("[" + ",".join(q) + "]")
        else:
            q.reverse()
            print("[" + ",".join(q) + "]")
    
    
    
        

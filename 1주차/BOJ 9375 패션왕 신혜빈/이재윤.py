// 파이썬 dictionary 사용법을 익혀야 한다 

T = int(input())


for i in range(T):
    n = int(input())
    dict={}
    
    sum = 1
    
    for j in range(n):
        name, type = map(str, input().split())
        
        if type in dict:
            dict[type] += 1
        else:
            dict[type] = 1
            
    for key in dict:
        sum *= (dict[key]+1)
        
    print(sum-1)

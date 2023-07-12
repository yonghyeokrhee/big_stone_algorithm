import math 

T = int(input())

for i in range(T):
    
    PS = input()
    stk = [] 
    isRight = True 
    
    for c in PS:
        if c == '(':
            stk.append(c)
        else:
            if len(stk) == 0:
                isRight = False
                break 
            stk.pop(len(stk)-1)
            
    if len(stk) != 0:
        isRight = False 
    
    if isRight == True:
        print("YES")
    else:
        print("NO")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



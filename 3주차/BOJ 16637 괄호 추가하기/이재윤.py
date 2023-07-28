// 코드를 좀 더 효율화해보자 

N = int(input())

expression = input()
maxCurr = -int(1e9)


def dfs(pos, curr):
    
    global maxCurr
    
    if pos >= (N+1):
        maxCurr = max(maxCurr, curr)
        return 
        
      
    if pos == 0:
        dfs(pos+2, curr)
    else:
        
        next = 0
        
        if expression[pos-1] == '+':
            next = curr + int(expression[pos])
        elif expression[pos-1] == '-':
            next = curr - int(expression[pos])
        elif expression[pos-1] == '*':
            next = curr * int(expression[pos])
        
        dfs(pos+2, next)
        
        if pos <= N-3:
            
            if expression[pos+1] == '+':
                next = int(expression[pos]) + int(expression[pos+2])
            elif expression[pos+1] == '-':
                next = int(expression[pos]) - int(expression[pos+2])
            elif expression[pos+1] == '*':
                next = int(expression[pos]) * int(expression[pos+2])
            
            
            if expression[pos-1] == '+':
                next = curr + next
            elif expression[pos-1] == '-':
                next = curr - next
            elif expression[pos-1] == '*':
                next = curr * next
            
            dfs(pos+4, next)




dfs(0, int(expression[0]))



print(maxCurr)

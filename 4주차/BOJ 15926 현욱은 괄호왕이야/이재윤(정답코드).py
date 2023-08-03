// 스택에 위치를 저장해놓는다는 개념이 중요하다 

n = int(input())

row = input()
start = 0
end = 0 

arr = [0]*n

stk = []

for i in range(0, n):
    
    if row[i] == '(':
        stk.append(('(', i))
        
    elif row[i] == ')':
        if len(stk) >= 1:
            c, pos = stk.pop(len(stk)-1)
            arr[pos] += 1
            arr[i] += 1
        
longest = 0 
currLen = 0

for i in range(0, len(arr)):
    if arr[i] == 1:
        currLen += 1 
    else:
        longest = max(longest, currLen)
        currLen = 0 
        
longest = max(longest, currLen)        
print(longest)
            
            
            
            
            

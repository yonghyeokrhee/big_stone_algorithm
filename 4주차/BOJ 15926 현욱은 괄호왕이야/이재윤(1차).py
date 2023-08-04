n = int(input())

row = input()
start = 0
end = 0 

arr = [0]*n

stk = []

for i in range(0, n):
    
    if row[i] == '(':
        if len(stk) == 0:
            start = i
        
        stk.append('(')
        
    elif row[i] == ')':
        if len(stk) >= 1:
            stk.pop(len(stk)-1)
            
            if len(stk) == 0:
                end = i 
                print(i, start, end)
                
                for j in range(start, end+1):
                    arr[j] += 1 
                    
        
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
            
            
            
            
            

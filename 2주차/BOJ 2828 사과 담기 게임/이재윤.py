N, M = map(int, input().split())

start = 1
end = 1+M-1
move = 0 

j = int(input())

for i in range(j):
    num = int(input())
    
    if start<=num and num <= end:
        continue
    elif num < start:
        move += (start-num)
        end -= (start-num)
        start = num
    elif num > end:
        move += (num-end)
        start += (num-end)
        end = num  
        
print(move)
        
        
        
        
    
    
    
    
    
    

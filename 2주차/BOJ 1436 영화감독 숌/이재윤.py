// 좀 더 효율적인 코드를 작성해보자 

import sys

input = sys.stdin.readline

N = int(input())

num = 1 
order = 0 

while True:
    
    numStr = str(num)
    
    if numStr.count('666') >= 1:
        order += 1 
        
    if order == N:
        break 
    
    num += 1 

print(num)







        
        
        
        
    
    

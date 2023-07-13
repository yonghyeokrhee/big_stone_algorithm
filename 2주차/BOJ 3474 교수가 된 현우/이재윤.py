// import sys와 input = sys.stdin.readline을 추가해야 한다 

import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    num = int(input())
    cnt5 = 0
    num5 = 5 
    
        
    while True:
        if num < num5:
            break
        cnt5 += int(num//num5)
        num5 *= 5 
        
    print(cnt5)

        
        
        
        
    

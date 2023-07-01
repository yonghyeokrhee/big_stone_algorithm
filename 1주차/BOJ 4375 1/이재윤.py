// n을 1, 11, 111 이렇게 바꾸는 방식으로 접근해야 효율적이다 

while True:
    
    try:
        num = int(input())
    except:
        break
    
    n = 1
    
    while True:
        if n % num == 0:
            print(len(str(n)))
            break
        else:
            n = n*10+1
    
        

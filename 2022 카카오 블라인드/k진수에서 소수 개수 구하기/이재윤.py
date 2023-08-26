import math

def getNumber(n, k):
    
    res = ""
    
    while True:
        
        if n == 0:
            break
        
        remain = n % k 
        
        res += str(remain)
        
        n = int(n // k)

    return res[::-1]


def isPrime(num):
    
    
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
            
    return True



def solution(n, k):
    answer = 0
    
    res = getNumber(n, k)
    
    tmp = ""
    ans = []
    
    for i in range(0, len(res)):
        c = res[i]
        if c == '0':
            if len(tmp) != 0:
                ans.append(tmp)
                tmp = ""
        else:
            tmp += c
    
    
    if len(tmp) != 0:
        ans.append(tmp)
        
    
    for num in ans:
        num = int(num)
        if num == 1:
            continue
        
        if isPrime(num) == True:
            answer += 1 
        
        

    return answer

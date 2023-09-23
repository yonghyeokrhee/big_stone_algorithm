def binarySearch(start, end, res, flag):
    

    if flag == False and start == end:
        return True
        
    if flag == True and start == end:
        if res[start] == '1':
            return False
        else:
            return True 
            
    mid = (start+end) // 2 
    if flag == True and res[mid] == '1':
        return False 
        
    
    if res[mid] == '1':
        return binarySearch(start, mid-1, res, False) and binarySearch(mid+1, end, res, False)
    else:
        return binarySearch(start, mid-1, res, True) and binarySearch(mid+1, end, res, True)
    
    
    
    
    
    



def changeToBinary(num):
    
    res = ""
    
    while num != 0:
        
        r = num % 2 
        
        res += str(r)
        
        num = num // 2 

    binaryLen = len(res)
    
    n = 0
    m = 1 
    
    while True: 
        
        N = 2**n-1
        M = 2**m-1 
        
        if N < binaryLen and binaryLen <= M:
            if binaryLen == M:
                break
            else:
                gap = M-binaryLen 
                
                for i in range(gap):
                    res += '0'
                
                break     
        else:
            n += 1 
            m += 1 
    
    
    
        
    return res[::-1]


def solution(numbers):
    
    answer = []
    
    for num in numbers:
        res = changeToBinary(num)
        ## print(res)
        ## print(len(res))
        ans = binarySearch(0, len(res)-1, res, False)
        
        if ans == True:
            answer.append(1)
        else:
            answer.append(0)
            
    
        
    return answer 

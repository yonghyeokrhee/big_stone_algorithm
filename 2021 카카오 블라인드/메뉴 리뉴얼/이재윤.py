
info = {}

def check(curr, orders):

    cnt = 0 

    for order in orders:
        
         all_chars_included = all(char in order for char in curr)
            
         if all_chars_included:
                cnt += 1 
        
    if cnt >= 2:
        return True
    else:
        return False

    


def dfs(curr, course, orders):
    
    if len(curr) in course:
        
        cnt = 0 
        
        for order in orders:
            
            all_chars_included = all(char in order for char in curr)
            
            if all_chars_included:
                cnt += 1 
        
        if cnt >= 2:
            info[curr] = cnt 
        
    
    res = check(curr, orders)
    
    if res == False:
        return 
        

    
    
    if len(curr) != 0:
        last = ord(curr[-1])-65+1
    else:
        last = 0
        
    for i in range(last, 26):
        curr += chr(i+65)
        dfs(curr, course, orders)
        curr = curr[:-1]


def solution(orders, course):
    ans = []

    dfs("", course, orders)
    
    maxCnts = [0]*30

    for key in info:
        keyLen = len(key)
        cnt = info[key]

        if maxCnts[keyLen] == 0:
            maxCnts[keyLen] = cnt
        else:
            if maxCnts[keyLen] < cnt:
                maxCnts[keyLen] = cnt 

                
    for key in info:
        keyLen = len(key)
        cnt = info[key]

        if cnt == maxCnts[keyLen]:
            ans.append(key)

    
    return ans

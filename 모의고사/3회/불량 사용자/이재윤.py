

check = [False]*10
ans = 0 
selected = [] 


def isMapping(curr, user_id):
    
    
    if len(curr) != len(user_id):
        return False
        
        
    currLen = len(curr)
    
    
    for i in range(currLen):
        if curr[i] == '*':
            continue
        
        if curr[i] != user_id[i]:
            return False
            
            
    
    return True
    
    



def dfs(pos, banned_id, user_id, arr):
    
    global ans
    
    if pos == len(banned_id):
        s = ''
        for i in range(len(arr)):
            s += str(arr[i])
            
        s2 = sorted(s)			 
        s3 = ''.join(sorted(s))	
        
        if s3 not in selected:
            ans += 1 
            selected.append(s3)
        return 
        
        
    curr = banned_id[pos]
    
    
    for i in range(len(user_id)):
        if check[i] == False and isMapping(curr, user_id[i]):
            check[i] = True
            arr.append(i)
            dfs(pos+1, banned_id, user_id, arr)
            arr.pop(len(arr)-1)
            check[i] = False
    
    


def solution(user_id, banned_id):
    answer = 0
    
    arr = [] 
    dfs(0, banned_id, user_id, arr)
    
    
    answer = ans 
    
    return answer
    

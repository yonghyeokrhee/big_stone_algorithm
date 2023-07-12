// rs, cs, len으로 변수를 놓는 것이 좋다 

N = int(input())
arr = [] 


def isSame(rs, cs, len):
    global arr 
    
    num = arr[rs][cs]
    check = True 
    
    for i in range(rs, rs+len):
        for j in range(cs, cs+len):
            if arr[i][j] != num:
                check = False 
                
    return check 
    



def recursive(rs, cs, len):
    
    res = isSame(rs, cs, len)
    
    
    if res == True:
        return str(arr[rs][cs])
    
    
    return '(' + recursive(rs, cs, len//2) + recursive(rs, cs+len//2, len//2) + recursive(rs+len//2, cs, len//2) + recursive(rs+len//2, cs+len//2, len//2) + ')'
    
        
    
    
for i in range(N):
    tmp = list(map(int, input()))
    arr.append(tmp)
    

res = recursive(0, 0, N)
print(res) 


    
    
    
    
    
    
    
    
    
    
    
    



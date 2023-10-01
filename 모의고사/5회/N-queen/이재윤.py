N = int(input())


ans = 0 


def check(row, col, checked, N):
    
    for x, y in checked:
        if abs(x-row) == abs(y-col):
            return False
            
    return True
    
  

def dfs(row, cols, checked, N):
    
    global ans 
    
    if row == N+1:
        ans += 1 
        return 
      
    for i in range(1, N+1):
        if cols[i] == False and check(row, i, checked, N):
            cols[i] = True
            checked.append((row, i))
            dfs(row+1, cols, checked, N)
            checked.pop(len(checked)-1)
            cols[i] = False
    
    
    
cols = [False]*(N+1)
checked = []

dfs(1, cols, checked, N)


print(ans)

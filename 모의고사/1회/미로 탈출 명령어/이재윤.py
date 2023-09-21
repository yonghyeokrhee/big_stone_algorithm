import sys
sys.setrecursionlimit(10**6)

dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
answer = ''

def dfs(n, m, x, y, str, r, c, k):

    global answer
    
    if answer != '':
        return 
    
    if len(str) > k:
        return 

    if len(str) == k and x == r and y == c:
        
        if answer == '':
            answer = str
        else:
            answer = min(answer, str)
        return 
    
    
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
    
        if 0<=nx and nx < n and 0<= ny and ny<m:
            
            if i == 0:
                str += 'd'
            elif i == 1:
                str += 'l'
            elif i == 2:
                str += 'r'
            elif i == 3:
                str += 'u'
                
            dfs(n, m, nx, ny, str, r, c, k)
            
            str = str[:-1]
            
            
    


def solution(n, m, x, y, r, c, k):
    
    str = ''
    dfs(n, m, x-1, y-1, str, r-1, c-1, k)
    
    if answer == '':
        return "impossible"
    else:
        return answer
    

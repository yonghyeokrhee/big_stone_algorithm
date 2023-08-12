N, K = map(int, input().split())

check = [False]*30

words = []

for i in range(N):
    word = input()
    words.append(word)
    
maxCnt = 0
ans = [] 

def dfs(pos, cnt):
    
    
    global maxAns 
    
    if (pos>=1 and check[0] == False) or (pos>=3 and check[2] == False) or (pos >= 9 and check[8] == False) or (pos>=14 and check[13] == False) or (pos >= 20 and check[19] == False):
        return 
    
    
    if cnt == K:
        
        
        if check[0] == True and check[2] == True and check[8] == True and check[13] == True and check[19] == True:
            
            newStr = ''
            for i in range(26):
                if check[i] == True:
                    newStr += chr(i+97)
            
            ans.append(newStr)
            
        return 
    
    if pos == 26:
        return 
    
   
    check[pos] = True
    dfs(pos+1, cnt+1)
    check[pos] = False
    dfs(pos+1, cnt)
    
    
    
if K <= 4:
    print(0)
else:
    dfs(0, 0)
    
    for tmp in ans: 
        
        cnt = 0 
        check = [0]*26
        
        for c in tmp:
            pos = ord(c)-97
            check[pos] += 1 
        
        for word in words: 
            
            isAble = True
            for c in word:
                pos = ord(c)-97
                if check[pos] == 1:
                    continue
                else:
                    isAble = False
                    break
            
            if isAble == True:
                cnt += 1
                
        maxCnt = max(maxCnt, cnt)
        
    print(maxCnt)
    
    
    

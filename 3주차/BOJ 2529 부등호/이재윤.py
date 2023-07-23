// 리턴문의 위치에 주의해야 한다 

k = int(input())
check = [False]*10

symbols = list(input().split())
maxNum = -int(1e12)
minNum = int(1e12)


def dfs(pos, arr):
    
    global maxNum
    global minNum
    
    if pos == k+1:
        numStr = ''
        for i in arr:
            numStr += str(i)
        num = int(numStr)
        
        maxNum = max(maxNum, num)
        minNum = min(minNum, num)
        
        return 
        
    
    last = arr[len(arr)-1]
    
    
    for i in range(0, 10):
        if check[i] == False:
            if (symbols[pos-1] == '<' and last < i) or (symbols[pos-1] == '>' and last > i):
                check[i] = True
                arr.append(i)
                dfs(pos+1, arr)
                arr.pop(len(arr)-1)
                check[i] = False 
    
                
            

arr = []

for i in range(0, 10):
    if check[i] == False:
        check[i] = True
        arr.append(i)
        dfs(1, arr)
        arr.pop(len(arr)-1)
        check[i] = False
        

print(maxNum)
if len(str(minNum)) == k:
    minNumStr = '0' + str(minNum)
    print(minNumStr)
else:    
    print(minNum)





    

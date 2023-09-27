import copy

check = [False]*3 
maxNum = 0


def getSum(expression, choose):
    
    global maxNum 
    
    nums = [] 
    symbols = []
    str = ''
    
    for c in expression:
        if c == '*' or c == '+' or c == '-':
            nums.append(int(str))
            str = ''
            symbols.append(c) 
        else:
            str += c 
            
            
    nums.append(int(str))
            
            
            
    for i in range(0, 3): 
        
        pos = choose[i] 
        newNums = []
        newSymbols = [] 
        newNums.append(nums[0])
        if pos == 0:
            
            for j in range(len(symbols)):
                if symbols[j] == '*':
                    num = nums[j+1]
                    newNum = newNums[len(newNums)-1]*int(num)
                    newNums[len(newNums)-1] = newNum
                else:
                    newSymbols.append(symbols[j])
                    newNums.append(nums[j+1])
                    
        elif pos == 1:
            
            for j in range(len(symbols)):
                if symbols[j] == '+':
                    num = nums[j+1]
                    newNum = newNums[len(newNums)-1]+int(num)
                    newNums[len(newNums)-1] = newNum
                else:
                    newSymbols.append(symbols[j])
                    newNums.append(nums[j+1])
            
            
        
        elif pos == 2:
            
            for j in range(len(symbols)):
                if symbols[j] == '-':
                    num = nums[j+1]
                    newNum = newNums[len(newNums)-1]-int(num)
                    newNums[len(newNums)-1] = newNum
                else:
                    newSymbols.append(symbols[j])
                    newNums.append(nums[j+1])
        
        
        nums = copy.deepcopy(newNums)
        symbols = copy.deepcopy(newSymbols)
        
        
    maxNum = max(maxNum, abs(nums[0]))
        
            
        
            

def dfs(expression, choose):
    
    if len(choose) == 3:
        getSum(expression, choose)
        return 
        
        
        
    for i in range(3):
        if check[i] == False:
            check[i] = True
            choose.append(i)
            dfs(expression, choose)
            choose.pop(len(choose)-1)
            check[i] = False
    
    
    
    
    
def solution(expression):
    answer = 0
    choose = []
    dfs(expression, choose)
    answer = maxNum 
    return answer
    

import copy

check = [False]*3 
maxNum = 0
initNums = []
initSymbols = [] 

def initialize(expression):
    
    str = ''
    
    
    for c in expression:
        if c == '*' or c == '+' or c == '-':
            initNums.append(int(str))
            str = ''
            initSymbols.append(c) 
        else:
            str += c 
            
            
    initNums.append(int(str))
    


def getSum(expression, choose):
    
    global maxNum 
    
    nums = copy.deepcopy(initNums)
    symbols = copy.deepcopy(initSymbols)
                    
    for i in range(0, 3): 
        
        pos = choose[i] 
        newNums = []
        newSymbols = [] 
        newNums.append(nums[0])
        target = ''
        
        if pos == 0:
            target = '*'
        elif pos == 1:
            target = '+'
        elif pos == 2:
            target = '-'
        
            
        for j in range(len(symbols)):
            if symbols[j] == target:
                num = nums[j+1]
                newNum = 0
                if target == '*':
                    newNum = newNums[len(newNums)-1]*int(num)
                elif target == '+':
                    newNum = newNums[len(newNums)-1]+int(num)
                elif target == '-':
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
    initialize(expression)
    dfs(expression, choose)
    answer = maxNum 
    return answer

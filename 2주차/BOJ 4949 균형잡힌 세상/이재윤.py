


while True:
    
    stack = []
    
    sentence = input()
    
    if sentence == '.':
        break 
    
    isBalanced = True 
    
    for c in sentence: 
        
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')':
            // len을 판단하는 것이 매우 중요하다 
            if len(stack) != 0 and stack[len(stack)-1] == '(':
                stack.pop(len(stack)-1)
            else:
                isBalanced = False
                break 
        elif c == ']':
            // len을 판단하는 것이 매우 중요하다 
            if len(stack) != 0 and stack[len(stack)-1] == '[':
                stack.pop(len(stack)-1)
            else:
                isBalanced = False
                break
            
    if len(stack) != 0:
        isBalanced = False 
        
    
    if isBalanced == True:
        print("yes")
    else:
        print("no")
    
    
    
    

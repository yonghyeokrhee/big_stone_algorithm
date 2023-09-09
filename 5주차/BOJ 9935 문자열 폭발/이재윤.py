sentence = input()

fire = input()
fireLen = len(fire)

stack = [] 

for c in sentence:
    
    stack.append(c)
    stackLen = len(stack)
    
    if stackLen >= fireLen:
        tmp = ''.join(stack[stackLen-fireLen:])
        if tmp == fire:
            for i in range(fireLen):
                stack.pop(len(stack)-1)
        
    
if len(stack) == 0:
    print("FRULA")
else:
    print(''.join(stack))
    
    

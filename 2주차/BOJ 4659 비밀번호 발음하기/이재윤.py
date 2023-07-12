// 에지 케이스에 대해 주의해야 한다 

def isRight(password):
    
    vowelCnt = 0 
    
    check2 = True
    check3 = True 
    vowel = 0
    conso = 0 
    
    for c in password:
        
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c =='u':
            vowelCnt += 1
            vowel += 1
            conso = 0 
        else:
            vowel = 0 
            conso += 1
            
        if vowel >= 3 or conso >= 3:
            check2 = False
            break 
            
    for i in range(1, len(password)):
        if password[i-1] == password[i]:
            if password[i-1] == 'e' or password[i-1] == 'o':
                continue
            else:
                check3 = False
                break 
    
    return vowelCnt >= 1 and check2 and check3   
    


while True: 
    
    password = input()
    
    if password == 'end':
        break 
    
    res = isRight(password)
    
    if res == True:
        print("<" + password + "> " + "is acceptable.")
    else:
        print("<" + password + "> " + "is not acceptable.")
    
    
    
    
    
    
    




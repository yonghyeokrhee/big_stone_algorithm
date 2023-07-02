// 문제에서의 입력값을 정확히 입력해야 한다 

name = input()
arr = [0]*30

ans = ""
odd = 0
oddPos = -1

for c in name:
    pos = ord(c)-65
    arr[pos] += 1
    
for i in range(0, 26):
    if arr[i] % 2 == 1:
        odd += 1
        oddPos = i
        
        
if odd>=2:
    print("I'm Sorry Hansoo")
else:
    if oddPos != -1:
        oddPosCnt = arr[oddPos]
        ans += chr(oddPos+65)
        arr[oddPos] -= 1
        
    for i in range(25, -1, -1):
        cnt = arr[i]
    
        if cnt == 0 or cnt % 2 == 1:
            continue
        else:
            for j in range(cnt//2):
                ans = chr(i+65) + ans
            
            for j in range(cnt//2):
                ans += chr(i+65)
                
print(ans)    

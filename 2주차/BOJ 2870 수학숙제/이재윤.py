
M = int(input())
arr = [] 


for i in range(M):
    tmp = '' 
    number = input()
    for c in number:
        if '0' <= c and c <= '9':
            tmp += c 
        else:
            if tmp != '':
                arr.append(int(tmp))
                tmp = ''
    
    if tmp != '':
        arr.append(int(tmp))
    
arr.sort()

for num in arr:
    print(num)




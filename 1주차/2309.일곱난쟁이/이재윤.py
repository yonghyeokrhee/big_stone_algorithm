arr = []
seven = [] 
sum = 0
diff = 0
pos1 = 0
pos2 = 0

for i in range(9):
    num = int(input())
    arr.append(num)
    sum += num
    
diff = sum-100

for i in range(9):
    for j in range(i+1, 9):
        if arr[i]+arr[j] == diff:
            pos1 = i
            pos2 = j
            
            
for i in range(9):
    if i == pos1 or i == pos2:
        continue
    else:
        seven.append(arr[i])
        
seven.sort()

for num in seven:
    print(num, end='\n')

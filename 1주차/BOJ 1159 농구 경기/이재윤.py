## template

N = int(input())
arr = []

for i in range(N):
 name = input()
 arr.append(name)
 
arr.sort()
arrLen = len(arr)
cnt = 1
ans = "" 

for i in range(1, arrLen):
    // 첫 글자끼리 비교를 해야 한다 
    if arr[i-1][0] == arr[i][0]:
        cnt += 1
    else:
        if cnt >= 5:
            ans += arr[i-1][0]
        cnt = 1 

// 이 케이스를 반드시 포함시켜야 한다 
if cnt >= 5:
    ans += arr[arrLen-1][0]
              
        
if ans == '':
    print("PREDAJA")
else:
    tmp = list(ans)
    tmp.sort()
    ans = ''.join(tmp)
    print(ans)



 

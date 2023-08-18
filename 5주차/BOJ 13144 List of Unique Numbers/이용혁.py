n = int(input())
arr = [*map(int,input().split())]

# 가장 멀리갈 수 있는 unique 한 배열의 끝을 찾아본다.
mem = [0] * 100001
e = 0
s = 0
ret = 0
while e < n:
    if not mem[arr[e]]:
        mem[arr[e]] +=1
        e +=1
    else:
        ret += (e-s)
        mem[arr[s]] -= 1
        s+=1

ret += ((e-s) * (e-s+1)) // 2
print(ret)

// 파이썬에서 문자를 숫자로 변환하려면, ord()를 사용하면 된다 

str = input()

arr = [0]*30

for c in str:
    pos = ord(c)-97
    arr[pos] += 1
    

for i in range(26):
    print(arr[i], end=' ')

// 아스키코드 문자를 숫자로 변환할 때는 ord를 
// 숫자를 아스키코드 문자로 변환할 때는 chr를 사용한다 

## template
A = input()
ans = "" 

for c in A: 
   if 65<=ord(c) and ord(c) <=90:
    tmp = ord(c)
    tmp += 13
    if tmp >= 91:
       tmp -= 26
    ans += chr(tmp) 
   elif 97<=ord(c) and ord(c) <=122:
    tmp = ord(c) 
    tmp += 13 
    if tmp >= 123:
       tmp -= 26
    ans += chr(tmp) 
   else:
    ans += c

print(ans)

 

ps = input()

char  = [0] * 26
for c in ps:
    char[ord(c) - 65] += 1

flag = 0
mid = ''
for i in range(len(char)):
    if char[i] % 2 == 1:
        flag += 1
        mid += chr(i+ 65)
        char[i] -= 1
if flag > 1:
    print("I'm Sorry Hansoo")

else:
    for i in range(len(char)-1,-1,-1):
        while char[i]:
            mid += chr(i+65)
            mid = chr(i+65) + mid
            char[i] -= 2
    print(mid)
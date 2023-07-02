tc = input()
answer = ''
for i in tc:
    if i.isalpha() and i.isupper():
        answer += chr(((ord(i) - 65) + 13 ) % 26 + 65)
    elif i.isalpha():
        answer += chr(((ord(i) - 97) + 13 ) % 26 + 97)
    else:
        answer += i
print(answer)
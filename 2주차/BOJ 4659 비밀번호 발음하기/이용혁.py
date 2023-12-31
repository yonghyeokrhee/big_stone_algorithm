while True:
    s = input()
    if s == 'end':
        break
    vowel = 0
    conso = 0
    check1 = False
    check2 = True
    check3 = True
    for i in range(len(s)):
        if s[i] in 'aeiou':
            check1 = True
            vowel += 1
            conso = 0
        else:
            vowel = 0
            conso += 1
        if vowel >= 3 or conso >= 3:
            check2 = False
            break
        if i > 0 and s[i] == s[i-1] and s[i] not in 'eo':
            check3 = False
            break
    if check2 and check3 and check1:
        print(f'<{s}> is acceptable.')
    else:
        print(f'<{s}> is not acceptable.')

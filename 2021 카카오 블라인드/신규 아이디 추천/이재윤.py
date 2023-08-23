def solution(new_id):
    answer = ''
    
    tmp = ""

    for c in new_id:

        if c.isupper():
            tmp += c.lower()
        else:
            tmp += c

    new_id = tmp     

    tmp = ""

    for c in new_id: 
        if c.islower() or c.isdigit() or c == '-' or c == '_' or c =='.':
            tmp += c
        else:
            continue

    new_id = tmp
    tmp = ""

    cnt = 0 
    for c in new_id: 
        if c == '.':
            cnt += 1 
        else:
            if cnt >= 1:
                tmp += '.'

            tmp += c
            cnt = 0 

    if cnt >= 1:
        tmp += '.'        


    new_id = tmp

    if len(new_id) != 0 and new_id[0] == '.':
        new_id = new_id[1:]

    if len(new_id) != 0 and new_id[len(new_id)-1] == '.':
        new_id = new_id[:-1]

    if len(new_id) == 0:
        new_id += 'a'

    if len(new_id) >= 16:
        new_id = new_id[0:15]

    if new_id[len(new_id)-1] == '.':
        new_id = new_id[:-1]

    if len(new_id) <= 2:
        c = new_id[-1]

        while len(new_id) != 3:
            new_id += c 

    answer = new_id
    
    
    
    return answer

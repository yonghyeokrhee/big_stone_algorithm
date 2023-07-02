from collections import deque
dq = deque()

ps = input()
for i in ps:
    dq.append(i)
    
if len(ps) == 1:
    print('1')
else:
    while len(dq)>1:
        l,r =  dq.popleft(), dq.pop()
        if l == r:
            continue
        else:
            break
    if len(dq) <= 1 and l == r:
        print('1')
    else:
        print('0')
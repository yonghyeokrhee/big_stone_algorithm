import sys
input = sys.stdin.readline
n= int(input())
s = 0
for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'add': #비트 켜기
        s = s |(1 << int(cmd[1])-1)
    elif cmd[0] == 'remove': #비트 끄기
        s = s & ~(1<<int(cmd[1])-1)
    elif cmd[0] == 'check': # 비트 확인
        print(1 if s & (1 << int(cmd[1])-1) else 0)
    elif cmd[0] == 'toggle': # 비트 전환
        s = s ^ (1 << int(cmd[1])-1)
    elif cmd[0] == 'all':
        s = (1<<20) -1
    elif cmd[0] == 'empty':
        s = 0

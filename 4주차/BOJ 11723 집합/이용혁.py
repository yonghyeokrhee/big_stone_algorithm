n = int(input())
print(n)
s = 0
for _ in range(n):
    cmd = input().split()
    print(f"this time cmd is : {cmd}")
    if cmd[0] == 'add': #비트 켜기
        print("비트켜기", int(cmd[1]))
        s = s |(1 << int(cmd[1])-1)
    elif cmd[0] == 'remove': #비트 끄기
        s = s & ~(1<<int(cmd[1])-1)
    elif cmd[0] == 'check': # 비트 확인
        print(1 if s & (1 << int(cmd[1])-1) else 0)
    elif cmd[0] == 'toggle': # 비트 전환
        s = s ^ (1 << int(cmd[1])-1)
    elif cmd[0] == 'all':
        print("모든 비트 켜기")
        s = (1<<20) -1
        print(bin(s))
    elif cmd[0] == 'empty':
        print("모든 비트 끄기")
        s = 0
        print(bin(s))

    print(f"{_} 번째 연산 끝")
import sys
input=sys.stdin.readline
n = int(input())
answer = 0

for _ in range(n):
    arr = list(input().rstrip())
    stack = []
    stack.append(arr.pop(0))
    # 두번째 부터..
    for a in arr:
        if stack and stack[-1]==a:
            stack.pop()
        else:
            stack.append(a)
    if not stack:
        answer += 1
print(answer)
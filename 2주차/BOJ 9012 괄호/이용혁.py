
def check(chars):
    stack = []
    for c in chars:
        if c == "(":
            stack.append(c)
        elif stack and c == ")":
            stack.pop()
        else:
            return False
    return not stack

for _ in range(int(input())):
    chars = input()
    if check(chars):
        print("YES")
    else:
        print("NO")
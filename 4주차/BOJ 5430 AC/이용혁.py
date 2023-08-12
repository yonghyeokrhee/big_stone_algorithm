from collections import deque
# reverse는 O(n) 이라서 reverse 함수를 쓰면 안됨.
T = int(input())

def R(arr:deque)->deque:
    global rev
    rev = ~rev

    #return arr

def D(arr:deque)->deque:
    global rev
    if rev:
        arr.pop()
    else:
        arr.popleft()

for i in range(T):
    try:
        F = input()
        N = int(input())
        arr = eval(input())
        arr = deque(arr)
        rev = err = False
        for f in F:
            eval(f)(arr)
        if rev:
            print("[" + ",".join(map(str, reversed(arr))) + "]")
        else:
            print("[" + ",".join(map(str,arr)) + "]")
    except:
        print("error")
from collections import deque

T = int(input())

def R(arr:deque)->deque:
    arr.reverse()

    #return arr

def D(arr:deque)->deque:
    arr.popleft()
    #return arr

for i in range(T):
    try:
        F = input()
        N = int(input())
        arr = eval(input())
        arr = deque(arr)
        for f in F:
            eval(f)(arr)
        print("[" + ",".join(map(str,arr)) + "]")
    except:
        print("error")
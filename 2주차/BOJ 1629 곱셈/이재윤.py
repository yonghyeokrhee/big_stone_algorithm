// memoization이 핵심인 문제이다.
// 이 부분에 대해 좀 더 제대로 이해해야겠다
// dictionary로 memoization을 할 수 있다
// 또한 B==1일 때도, A를 C로 modulo연산을 해야 한다 

import sys

input = sys.stdin.readline

def recursive(A, B, C, memo):
    
    if B == 1:
        return A % C
        
    if B in memo:
        return memo[B]
        
    if B % 2 == 1:
        memo[B] = (A*recursive(A, B//2, C, memo)*recursive(A, B//2, C, memo)) % C 
    else:
        memo[B] = (recursive(A, B//2, C, memo)*recursive(A, B//2, C, memo)) % C
    
    return memo[B]


a, b, c = map(int, input().split())

ans = recursive(a, b, c, {})

print(ans)










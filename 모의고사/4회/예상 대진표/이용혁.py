def solution(n,a,b):
    k = 1
    while a!=b:
        a = (a+1)//2
        b = (b+1)//2
        k += 1
    return k-1

print(solution(2,1,2)) # answer : 1
print(solution(4,2,4)) # answer : 2
print(solution(8,4,7,)) #answer : 3
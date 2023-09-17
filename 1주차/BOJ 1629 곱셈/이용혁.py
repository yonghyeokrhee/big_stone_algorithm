n,m,k = map(int, input().split())

def power(C, n):
    result = 1
    while n:
        if n % 2 != 0:
            result *= C
            result %= k
        C *= C
        C %= k
        n //= 2
    return result
if m == 1:
    print(n%k)
else:
    print(power(n,m))
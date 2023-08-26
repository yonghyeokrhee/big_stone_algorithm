def numberToBase(n, b):
    if n == 0:
        return [0]
    digits =[]
    while n:
        digits.append(int(n % b))
        n //= b
    return ''.join(map(str,digits[::-1]))

def check_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3,n):
            if n % i == 0:
                return False

    return True

def solution(n, k):
    answer = 0
    basek = numberToBase(n,k)
    print(basek)
    arr = basek.split('0')
    for i in arr:
        if len(i) > 0 and check_prime(int(i)):
            answer +=1

    return answer

if __name__ == "__main__":
    print(solution(100000000000000000000000,3))
    # print(solution(110011,10))

import math
def numberToBase(n, b):
    if n == 0:
        return [0]
    digits =[]
    while n:
        digits.append(int(n % b))
        n //= b
    return ''.join(map(str,digits[::-1]))

def check_prime(num):
    if num > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(math.sqrt(num / 2)) + 1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False

def solution(n, k):
    answer = 0
    basek = numberToBase(n,k)
    arr = basek.split('0')
    for i in arr:
        if len(i) > 0 and check_prime(int(i)):
            answer +=1

    return answer

if __name__ == "__main__":
    print(solution(1000000,3))
    # print(solution(110011,10))

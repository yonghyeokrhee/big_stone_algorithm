from itertools import permutations
N:int = int(input())
operator:list = input().split()

nums = [i for i in range(10)]


mx = 0
mn = 100000000
operation = ''



for c in permutations(nums,N+1):

    operatation =''
    for index in range(len(c)-1):
        operatation+= str(c[index])
        operatation+= operator[index]
    operatation += str(c[-1])

    if eval(operatation):
        string_num = int("".join(map(str,c)))
        num = int(string_num)
        mx = max(mx, num)
        mn = min(mn, num)
print(str(mx), str(mn) if mn > 100 else '0'+str(mn))
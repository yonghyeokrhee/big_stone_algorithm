from itertools import permutations
def solution(expression):
    # 가장 마지막 연산 순위를 기준으로 나누고 dfs 를 수행한다.

    def dfs(expression)->int:
        if expression.isdigit():
            return int(expression)

        for e in perm:
            for i in range(len(expression)-1,-1,-1):
                # print(expression[i])
                if expression[i] == e:
                    left = dfs(expression[:i])
                    right = dfs(expression[i+1:])
                else:
                    continue
                #print("this time operation is: ",eval(str(left) + e + str(right)))
                return eval(str(left) + e + str(right))

    operator = ["-","+","*"]
    sample = []
    mx = 0
    for o in operator:
        if o in expression:
            sample.append(o)
    for perm in permutations(sample):
        mx = max(mx,abs(dfs(expression)))
    return mx

expression = "100-200*300-500+20"
print(solution(expression))
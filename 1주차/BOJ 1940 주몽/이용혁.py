n = int(input())
m = int(input())
arr = list(map(int, input().split()))

# 앞에서 등장한 값이 배열에 들어있었는지를 확인하는 문제
# O(1)로 풀어야 함. (2초)
# 배열 문제임

# 필요한 수가 1000만 까지인데 고유한 수는 10만이면... 애초에 문제를 풀수 없는 경우도 있는거 아닌가?
# 그럼 바로 예외처리를 하는게 좋지 않을까?

bucket = [0] * 100000
answer = 0
if m >= 200000:
    print(0)
else:
    arr.sort()
    for a in arr:
        bucket[a] = 1
        if m-a == a:
            continue
        elif bucket[m -a]:
            answer += 1
    print(answer)
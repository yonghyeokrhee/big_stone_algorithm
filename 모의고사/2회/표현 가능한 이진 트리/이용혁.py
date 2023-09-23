
def binary_search(start, end, bi,flag)->bool:
    # flag가 있는 상태에서 array 안에 1이 존재하는 경우
    if flag and '1' in bi:
        return False
    # 끝까지 도달  한 경우
    if start == end-1:
        return True
    mid = (start + end) //2
    if not int(bi[mid]):
        flag = True

    return binary_search(start, mid, bi,flag) and binary_search(mid+1,end, bi,flag)


def solution(numbers):
    answer = []
    for num in numbers:
        bi = bin(num).split('b')[-1]
        n = 0
        while len(bi) > 2**n:
            n+=1
        # numbers to add prefix
        for _ in range(2**n-1 - len(bi)):
            bi = '0'+bi
        answer.append(binary_search(0,2**n-1, bi, False))
    return [*map(int,answer)]

print(solution([5]))
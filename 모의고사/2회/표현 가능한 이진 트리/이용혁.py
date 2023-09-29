import sys
sys.setrecursionlimit(1000000)
def binary_search(start, end, bi)->bool:
    mid = (start + end) //2
    # flag가 있는 상태에서 root node 좌우로 1이 있는 경우
    if start == end-1:
        return True
    if not bi[mid] and (bi[(start+mid)//2]==1 or bi[(mid+1+end)//2]==1):
        return False
    # 끝까지 도달  한 경우 node val은 0 또는 1이며 False를 반환한 적이 없으므로 문제가 없다.

    return binary_search(start, mid, bi) and binary_search(mid+1,end, bi)


def solution(numbers):
    answer = []
    for num in numbers:
        bi = bin(num).split('b')[-1]
        n = 0
        while len(bi) >= 2**n:
            n+=1
        # numbers to add prefix
        for _ in range(2**n-1 - len(bi)):
            bi = '0'+bi
        bi = [*map(int,list(bi))]
        answer.append(binary_search(0,2**n-1, bi))
    return [*map(int,answer)]
from collections import Counter, defaultdict

def check_unique(relation,candidate):
    if len(candidate)==0:
        return True
    keys = defaultdict(int)
    for row in relation:
        key = ''.join([row[cand] for cand in candidate])
        keys[key] +=1
        if keys[key] >=2:
            return False
    return True

def dfs(keys:list, candidates:list, relation,  k:int):
    """
    :param keys : 후보키를 만들 수 있는 bucket
    :param candidates: 후보키 리스트
    :param k: k는 후보키 조합의 개수
    :return:
    """
    if k == 0:
        return # w종료
    if check_unique(relation, candidates):
        answer.append(candidates[:])
        return # dfs 종료
    for i in keys:
        candidate = keys.pop(i)
        dfs(keys, candidates.append(candidate),relation , k-1)
        candidates.pop()
def solution(relation):
    cands = [i for i in range(len(relation[0]))]
    dfs(cands, [], relation, len(relation[0]))
    return answer
global answer
answer = []
print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))

from collections import Counter, defaultdict


def minimality(result):
    answer = []

    for x in result:

        flag = False

        for y in result:
            if x == y:
                continue
            else:
                if set(y).issubset(set(x)):
                    flag = True
                    break
        if flag:
            continue
        answer.append(x)
    return answer


def check_unique(relation, candidate):
    if len(candidate) == 0:
        return False
    keys = defaultdict(int)
    for row in relation:
        key = ''.join([row[cand] for cand in candidate])
        keys[key] += 1
        if keys[key] >= 2:
            return False
    return True


result = []


def mycombinations(arr, path, result, index, relation):
    if len(path) > 0 and check_unique(relation, path[:]):
        result.append(path[:])
        path[:].pop()
        return
    for i in range(index, len(arr)):
        path.append(arr[i])
        mycombinations(arr, path, result, i + 1, relation)
        path.pop()


def solution(relation):
    cands = [i for i in range(len(relation[0]))]
    mycombinations(cands, [], result, 0, relation)
    print(result)
    answer = minimality(result)
    print(answer)
    return len(answer)

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))




# 조합 만들기 (반드시 외워두자...)
# result = []
# def combinations(arr, path, result,index):
#     result.append(path[:])
#     for i in range(index, len(arr)):
#         path.append(arr[i])
#         combinations(arr, path, result,i+1)
#         path.pop()
#
# combinations([1,2,3],[],result,0)
# print(result)
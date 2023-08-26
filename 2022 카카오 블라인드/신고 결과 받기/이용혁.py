def solution(id_list, report, k):
    n = len(id_list)
    encoding = {i: j for i, j in zip(id_list, range(n))}
    arr = [[0] * n for _ in range(n)]
    arr2 = [k] * n

    for i in report:
        reporter, reportee = i.split()
        r1 = encoding[reporter]
        r2 = encoding[reportee]
        if not arr[r1][r2]:
            arr[r1][r2] +=1
        if arr2[r2] > 0:
            arr2[r2] -= 1

    answer = [0] * n
    print(arr)
    print(arr2)
    for j in range(n):
        for r in range(n):
            if arr[j][r]:
                if not arr2[r]:
                    answer[j] += 1
    return answer

if __name__ == "__main__":
    print(solution(["muzi", "frodo", "apeach", "neo"],\
             ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],\
             2))


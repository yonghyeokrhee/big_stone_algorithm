def solution(board, skill):
    sy = len(board)
    sx = len(board[0])

    arr = [[0]* sx for _ in range(sy)]

    for s in skill:

        if (s[0] - 1): # recover->True
            arr[s[1]][s[2]] += s[5]  # (y,x)
            if s[4] >= sx - 1 and s[3] >= sy - 1:
                continue
            if s[4] < sx - 1:
                arr[s[1]][s[4] + 1] -= s[5]
            if s[3] < sy - 1:
                arr[s[3] + 1][s[2]] -= s[5]
            if s[4] < sx - 1 and s[3] < sy - 1:
                arr[s[3] + 1][s[4] + 1] += s[5]
        else: # attack-> False
            arr[s[1]][s[2]] -= s[5]  # (y,x)
            if s[4] >= sx - 1 and s[3] >= sy - 1:
                pass
            if s[4] < sx - 1:
                arr[s[1]][s[4] + 1] += s[5]
            if s[3] < sy - 1:
                arr[s[3] + 1][s[2]] += s[5]
            if s[4] < sx - 1 and s[3] < sy - 1:
                    arr[s[3] + 1][s[4] + 1] -= s[5]

        # print("=========skill applied=========")
        # for a in arr:
        #     print(a)

    # 오른쪽으로 순회
    for j in range(sy):
        for i in range(1,sx):
            arr[j][i] += arr[j][i-1]


    # 아래쪽으로 순회
    for m in range(sx):
        for n in range(1,sy):
            arr[n][m] += arr[n-1][m]


    for k in range(sy):
        for j in range(sx):
            board[k][j] += arr[k][j]
    answer = 0

    for y in range(sy):
        for x in range(sx):
            if board[y][x] >= 1:
                answer += 1

    return answer

if __name__ == "__main__":
    print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))
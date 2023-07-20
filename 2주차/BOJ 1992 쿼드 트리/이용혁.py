N = int(input())
arr = [list(map(int,input())) for _ in range(N)]

def quard(x, y, N):
    """
    4분할로 쪼개서 들어가는 재귀문
    :param:
        x: 가장 왼쪽에서부터 0, 1, 2, 3, ...
        y : 가장 위에서부터 0 ,1, 2, 3, ...
    :return:
    """
    answer = ""
    pix = arr[y][x]
    half_n = int(N / 2)
    if not all([pix == arr[i][j] for j in range(x,x+N) for i in range(y,y+N)]):
        answer += "("
        answer += quard(x, y, half_n)
        answer += quard(x + half_n, y, half_n)
        answer += quard(x, y+ half_n, half_n )
        answer += quard(x+half_n, y+half_n, half_n)
        answer += ")"
        return answer
    elif all([pix == arr[i][j] for j in range(x,x+N) for i in range(y,y+N)]):
        answer = str(pix)
        return answer


print(quard(0, 0, N))
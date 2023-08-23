t, w = map(int, input().split())
arr = [int(input()) for _ in range(t)]

dp = [0] * (t +1)


for i in range(t):






def dfs(arr,ind,k,w)->int:
    """

    :param arr:
    :param ind:
    :param k: 자두가 서 있는 위치
    :return:
    """
    ret = 0
    # base case:
    if ind == len(arr)-1:
        dp[ind] =
        return 1 if -int(k)+2 == arr[ind] else 0
    if w == 0: #자두는 더 이상 움직일 수 없음.
        ret += dfs(arr[:ind], ind + 1, k, w)

    if -int(k)+2 == arr[ind]: # 자두가 서 있는 자리에 자두가 떨어진다.
        ret += 1
    else:  # 자두 자리에 떨어지지 않아. 이동하든 안하든 선택해야 함.
        ret += dfs(arr,ind+1,-k , w-1) + dfs(arr, ind+2, k, w) # 이동하고 cnt 하나 하자.

    return ret

print(dfs(arr,0,True, w))
n,k = map(int, input().split())
tcs = [input() for i in range(n)]

arr = [0] * 26

for s in ['a','n','t','i','c']:
    arr[ord(s)-97]=1

#추가로 조합 경우의 수를 arr에 넣는 코드가 필요하다.

    def dfs(indx, path, k):
        """
        기존에 있는 5개의 alphabet 을 제외하고 나머지 21개의 alphabet 중에서 3개에 해당하는 모든 경우를 추출하는 함수
        :param indx:
        :param path:
        :param k: 조합을 구성하는 요소의 개수
        :return: array of all possible combinations
        """
        if len(path) == k:
            result.append(path[:])
            return

        # alpha[i] 여기를 indx로 잘 못 표기해서 고생했음. 내일 기록해두자.
        # 그리고 index가 무한정 진행되지 않으려면 장치 하나 더 필요한듯.
        for i in range(indx, len(alpha)):
            path += [alpha[i]]
            dfs(i + 1, path, k)
            path.pop()
        return result

if k <5:
    print(0)
elif k == 5:
    cnt = 0
    for tc in tcs:
        if all([arr[ord(t) - 97] for t in tc]):
            cnt += 1
    print(cnt)
else:
    alpha = [i-97 for i in range(97,97+26) if chr(i) not in ['a','n','t','i','c']]
    result = []
    mx = 0
    comb = dfs(0, [], k - 5)

    for c in comb:
        new_arr = arr.copy()
        success = 0
        # 조합의 요소를 기존의 arr에 더하여 new_arr에 채워넣는다.
        for i in c:
            new_arr[i] = 1
        for tc in tcs:
            if len(tc) == 8:
                success +=1
            elif all([new_arr[ord(t)-97] for t in tc[4:-4]]):
                success += 1 #성공횟수 cnt
        if success > mx:
            mx = success # 최대 읽을 수 있는 단어 개수의 최대값을 udpate

    print(mx)
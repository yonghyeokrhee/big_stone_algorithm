from collections import defaultdict

def solution(n, info):
    global ryan, answer, mx
    ryan = [0]* len(info)
    answer = defaultdict(list)
    mx = 0
    
    def do_score(ryan, info):
        ryan_score = 0
        apeach_score = 0
        for i in range(11):
            if ryan[i] == 0 and info[i] == 0:
                continue
            elif ryan[i]>info[i]:
                ryan_score += 10-i
            else:
                apeach_score += 10-i
        if ryan_score > apeach_score:
            # print("==============start of the log=============")
            # print("ryan parameter", ryan)
            # print('ryan score is: ', ryan_score)
            return ryan_score - apeach_score
        return 0
           
    def dfs(idx,n):
        global mx
        if n <= 0: # 가지치기
            ryan_result = do_score(ryan,info)
            if ryan_result:
                # print("ryan's final score is: ", ryan_result)
                # print("no more left to shot")
                mx = max(mx, ryan_result)
                answer[ryan_result].append(ryan[:])
                # print("max:",mx)
                # print("ryan is : ", ryan)
            return
        if idx == 10:
            if n > 0:
                ryan[idx] += n
            ryan_result = do_score(ryan,info)
            if ryan_result:
                # print("this is the last of the target")
                mx = max(mx, ryan_result)
                answer[ryan_result].append(ryan[:])
                # print("max:",mx)
                # print("ryan is : ", ryan)
            ryan[idx] -= n
            return
        #print(ryan)
        winning=min(info[idx]+1,n)
        ryan[idx] += winning
        dfs(idx+1, n-winning)
        ryan[idx] -= winning
        dfs(idx+1, n)
        
    dfs(0,n)
    par = answer[mx]
    print(mx)
    print(par)
   
    return sorted(par, key = lambda x : x[::-1], reverse=True)[0] if par else [-1]

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
#print(solution(9,[0,0,1,2,0,1,1,1,1,1,1]))
#print(solution(1,[1,0,0,0,0,0,0,0,0,0,0]))
#print(solution(	10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))
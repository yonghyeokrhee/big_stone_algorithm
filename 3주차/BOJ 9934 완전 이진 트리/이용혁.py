from collections import defaultdict
K = int(input())
arr = list(map(int,input().split()))

# tree 자료 구조를 만든 다음에 거기에다가 넣는 방식으로 구현
# tree 자료 구조는 딕셔너리로 만들자.
tree = defaultdict(list)

def search_tree(start, end, d):

    # base case
    if d >= K:
        return # 종료시키기
    #leaf node
    if  start == end:
        tree[d].append(arr[start])
        return # 종료시키기

    middle = int((start + end)/2)



    tree[d].append(arr[middle])

    #왼쪽 탐색, 오른쪽 탐색
    search_tree(start, middle - 1, d + 1)
    search_tree(middle + 1, end, d + 1)



start = 0
end = len(arr) -1
search_tree(start, end, 0)

for i in range(K):
    print(' '.join(map(str,tree[i])))
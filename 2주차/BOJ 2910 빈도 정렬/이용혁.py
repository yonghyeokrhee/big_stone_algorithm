import collections

N, C = map(int, input().split())
arr = list(map(int, input().split()))

def freq(param):
    cnt = collections.Counter(arr)
    cnt_k_ord = [tp[0] for tp in cnt.most_common()]
    return cnt_k_ord.index(param)
answer= sorted(arr, key = freq)
print(" ".join(map(str,answer)))

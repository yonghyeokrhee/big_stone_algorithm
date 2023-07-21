import collections

N, C = 5, 2
arr = [1,1,1,2,2,2]


def freq(param):
    cnt = collections.Counter(arr)
    cnt_k_ord = [tp[0] for tp in cnt.most_common()]
    return cnt_k_ord.index(param)

print(sorted(arr, key = freq))

import itertools

arr = []
for _ in range(9):
    arr.append(int(input()))
arr.sort()
answer = 0
it = itertools.permutations(arr,7)

while answer != 100:
    dwarps = next(it)
    answer = sum(dwarps)
for i in dwarps:
    print(i)
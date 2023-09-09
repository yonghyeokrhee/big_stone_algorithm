string = input()
explosive = input()
explosive = list(explosive)
k = len(explosive)
arr = []

for i in range(len(string)):
    arr.append(string[i])
    if i-(k-1) >= 0 and arr[-k:] == explosive:
        for _ in range(k):
            arr.pop()

if arr:
    print(''.join(arr))
else:
    print('FRULA')
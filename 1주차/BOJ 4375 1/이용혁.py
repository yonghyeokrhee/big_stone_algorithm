import sys
input = sys.stdin.readlines
arr = [*map(int, input())]
#arr = input()
#print(arr)
for arg in arr:
    min_one = '1'
    while int(min_one)%arg:
        min_one+='1'
    print(len(min_one))

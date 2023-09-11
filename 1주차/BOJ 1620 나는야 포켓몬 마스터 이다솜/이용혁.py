import sys
from collections import defaultdict
input = sys.stdin.readline
N, M = map(int,input().split())
mylist = [None]*(N+1)
mydict=defaultdict(int)
for i in range(1,N+1):
    string = input().rstrip()
    mylist[i] = string
    mydict[string]=i
for _ in range(M):
    query = input().rstrip()
    if query.isdigit():
        print(mylist[int(query)])
    else:
        print(mydict[query])

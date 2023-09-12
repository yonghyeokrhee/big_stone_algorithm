import sys
n,m,k = map(int, input().split())
input = sys.stdin.readline

def sum(tree, i):
    ans = 0
    while i > 0:
        ans += tree[i]
        i -= (i&-i)
    return ans


def update(tree, i, diff):
    while i < len(tree):
        tree[i] += diff
        i += (i & -i)

a = [0] * (n+1)
tree = [0] * (n+1)

for i in range(1,n+1):
    a[i] = int(input())
    update(tree, i, a[i])

m+=k
while m:
    t1, t2, t3 = map(int, input().split())
    if t1 == 1:
        diff = t3- a[t2]
        a[t2] = t3
        update(tree, t2, diff)
    else:
        print(sum(tree, t3) - sum(tree, t2-1))
    m-=1
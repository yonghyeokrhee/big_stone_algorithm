import sys
import re 
ps = sys.stdin.readlines()
tcs = []
for i in ps:
    tcs.append(i.strip())
pt = tcs[1].split('*')
p = re.compile(r'^' + pt[0] + '.*' + pt[1] + '$')
for tc in tcs[2:]:
    if bool(re.search(p, tc)):
        print('DA')
    else:
        print('NE')
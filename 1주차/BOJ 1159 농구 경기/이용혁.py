from collections import Counter
import sys

lineup = []

doc = sys.stdin.readlines() 

for i in doc[1:]:
    lineup.append(i.strip()[0])


bucket = [0] * 26

for s in lineup:
    bucket[ord(s) - 97] += 1
s = ''
for i in range(len(bucket)):
    if bucket[i]>=5:
        s +=chr(i+97)
if s == '':
    print('PREDAJA')
else:
    print(s)
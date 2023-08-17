## 비트마스킹 풀이

n,k = map(int, input().split())
tcs = [input() for i in range(n)]

words = [0] * 51

for i in range(n):
    for char in tcs[i]:
        words[i] |= (1 << ord(char)-97) # 비트를 하나씩 계속 킨다. 안켜져 있으면 키고 켜져 있으면 내버려둔다. 비트를 키는 방식으로 켜야하는 알파벳을 업데이트를 한다.
        # 모든 알파벳의 비트가 다 켜진 상황은 2^26 -1 일 것이고 a 만켜져 잇으면 1, b만 켜져 있으면 2, ab 켜져있으면 3 이런식이다.
# 모든 테스트 케이스에 대한 비트 기록을 words 에 저장한 뒤에 조합을 뽑아서 검사한다.

def count(mask): # 마스킹 되어있는 비트를 출력한다.
    cnt = 0
    for tc in words:
        if tc and (tc & mask) == tc:
            cnt +=1
    return cnt

def go(index, k, mask):
    if (k<0):
        return 0
    if index == 26:
        return count(mask)
    ret = go(index+1, k-1, mask|1<<index)
    if (index != (ord('a') - 97) and index != (ord('n') - 97) and index != (ord('t') - 97) and index != (ord('i') - 97) \
and index != (ord('c') - 97)):
        ret = max(ret, go(index+1, k ,mask))
    return ret

print(go(0,k,0))
n = int(input())
stick = 64

cnt = 0
for i in range(7):
    half = stick >> i
    if n < half:
        continue
    if n >= half:
        cnt += 1 # 조각 하나 만들었음.
        n -= half
    if n == 0:
        break
print(cnt)
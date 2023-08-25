from math import ceil
c1, c2, c3, c4 = list(map(input().count, ['1', '2', '3', '4']))
print(c1,c2,c3,c4)

c1 = max(c1 - (c2 % 2) * 2 - c3, 0)
taxi_count = c4 + c3 + ceil(c2 / 2) + ceil(c1 / 4)

print(taxi_count)
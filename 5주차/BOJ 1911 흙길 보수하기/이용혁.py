N, L =  map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(N)]
arr.sort(key = lambda x: x[0]) # 먼저 웅덩이 시작점을 기준으로 한다.
s,e, cnt = 0,0,0
for elem in arr:
    if e < elem[0]:
        s = elem[0]
        e = s
        while e < elem[1]:
            cnt += 1
            e += L
    elif s <= elem[0] <= e:
        while e < elem[1]:
            cnt += 1
            e += L


# for elem in arr:
#     if elem[0] > e and elem[0]>=0: # 웅덩이 위치가 널빤지 종점보다 더 큰 상태로 시작점이 바뀌어야 한다.
#         s = elem[0]
#         if not (elem[1] - s) % L :
#             cnt += (elem[1] - s) // L
#             e = elem[1]
#         else:
#             cnt += (elem[1] - s) // L + 1
#             e = elem[1] - (elem[1] - s) % L + L
#             s = e - L
#     # elif elem[0]<e and elem[1]>=e: # 웅덩이 위치가  널빤지의 시점과 종점 가운데 위치한 상태로 널빤지를 하나 놓지만 시점과 종점은 이전 위치에서 L 만큼 연장될 뿐.
#     #     s = e
#     #     e += L
#     #     cnt += 1
#     # 다른 경우는 있을 수 없다. (반증 해보지 않음)
#     # 널빤지가 여전히 웅덩이를 다 커버하지 못하고 있다면 지속적으로 하나씩 더 놓아준다.
#     # 시간 초과의 원인을 탐색 - >  while 문의 존재 때문일 수 있다.
#     elif elem[1] > e and elem[0] >= s: # 중간에 걸쳐진 경우임.
#         if not (elem[1] - s) % L :
#             cnt += (elem[1] - s) // L
#             e = elem[1]
#         else:
#             cnt += (elem[1] - e) // L + 1
#             e = elem[1] - (elem[1] - e) % L + L
#     print(f"starting: ",s)
#     print(f"ending: ",e)
#     print(f"count is: ",cnt)

print(cnt)


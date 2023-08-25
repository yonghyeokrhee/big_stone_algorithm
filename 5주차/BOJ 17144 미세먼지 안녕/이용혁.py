R,C,T = map(int, input().split())
arr = [[*map(int,input().split())] for _ in range(R)]
narr = [[0]*C for _ in range(R)]

# 공기 청정기 위치 파악하기 (상, 하)
air = [(y,x) for x in range(C) for y in range(R) if arr[y][x] ==-1]

dy = [0,1,0,-1]
dx = [1,0,-1,0]
# 하루 동안 미세 먼지가 이동한다.
for y in range(R):
    for x in range(C):
        mise = arr[y][x] // 5
        if mise > 0:
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or nx < 0 or ny > R-1 or nx > C-1 or arr[ny][nx] == -1:
                    continue
                else:
                    narr[ny][nx] += mise
                    arr[y][x] -= mise

for y in range(R):
    for x in range(C):
        narr[y][x] += arr[y][x]

arr = narr

# 공기 청정기 바람 확산 로직
# 위쪽 공기청정기
air[0]
# 아래쪽 공기 청정기


for i in narr:
    print(i)

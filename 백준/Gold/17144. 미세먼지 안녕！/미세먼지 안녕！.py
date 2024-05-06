# 미세먼지 확산
def munjiDiff(temp, x, y):
        mj = arr[x][y]//5

        for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
            nr = x + dr
            nc = y + dc
            if 0 <= nr < r and 0 <= nc < c and arr[nr][nc] != -1 :
                temp[nr][nc] += mj
                temp[x][y] -= mj
                
def airOnTop(idx):
    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]
    d = 0
    prev = 0
    x, y = idx, 1
    while True:
        nx = x + dr[d]
        ny = y + dc[d]
        if x == idx and y == 0:
            break
        if 0 <= nx < r and 0 <= ny < c:
            arr[x][y], prev = prev, arr[x][y]
            x, y = nx, ny
        else:
            d += 1

def airOnBottom(idx):
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    d = 0
    prev = 0
    x, y = idx, 1
    while True:
        nx = x + dr[d]
        ny = y + dc[d]
        if x == idx and y == 0:
            break
        if 0 <= nx < r and 0 <= ny < c:
            arr[x][y], prev = prev, arr[x][y]
            x, y = nx, ny
        else:
            d += 1



r, c, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]

# 공기 청정기 위치 찾기
airL = []
for i in range(r):
    for j in range(c):
        if arr[i][j] == -1:
            airL.append((i, j))


time = 0
while time < t:
    temp = [[0 for _ in range(c)] for _ in range(r)] # 확산되는 먼지 기록용

    # 미세먼지 위치 찾기
    for i in range(r):
        for j in range(c):
            if arr[i][j] > 0:
                munjiDiff(temp, i, j)

    for i in range(r):
        for j in range(c):
            arr[i][j] += temp[i][j] # 처음 먼지 + 확산된 먼지


    # print(arr)
    # 공기 청정기 가동
    airOnTop(airL[0][0])
    airOnBottom(airL[1][0])
    time += 1

sumV = 0
for i in range(r):
    sumV += sum(arr[i])

print(sumV+2)

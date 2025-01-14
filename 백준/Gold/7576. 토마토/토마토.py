from collections import deque

import sys
input = sys.stdin.readline

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

def findMinDay() :
    while tomatoes :
        xr, xc = tomatoes.popleft()

        for dr, dc in [(0, 1), (1, 0),(0, -1), (-1, 0)] :
            nr = xr + dr
            nc = xc + dc
            if 0 <= nr < N and 0 <= nc < M and box[nr][nc] == 0 :
                box[nr][nc] = box[xr][xc] + 1
                tomatoes.append((nr, nc))

tomatoes = deque([])
cnt = 0
for r in range(N) :
    for c in range(M) :
        if box[r][c] == 1 :
            tomatoes.append((r,c))
            cnt += 1

if cnt == M*N :
    print(0)
    exit()
else:
    findMinDay()

maxDay = 0
for r in range(N) :
    for c in range(M) :
        if box[r][c] == 0 :
            print(-1)
            exit()
        else :
            maxDay = max(maxDay, box[r][c])
print(maxDay - 1)
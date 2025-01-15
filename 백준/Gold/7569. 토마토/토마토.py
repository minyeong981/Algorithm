from collections import deque

import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

def tomatoesRipen() :
    while tomatoes :
        h, r, c = tomatoes.popleft()

        for dh, dr, dc in [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)] :
            nh = h + dh
            nr = r + dr
            nc = c + dc
            if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M and box[nh][nr][nc] == 0 :
                box[nh][nr][nc] = box[h][r][c] + 1
                tomatoes.append((nh,nr,nc))

tomatoes = deque()
cnt = 0
for i in range(H) :
    for j in range(N) :
        for k in range(M) :
            if box[i][j][k] == 1 :
                tomatoes.append((i, j, k)) # h, r, c
                cnt += 1
if cnt == M*N*H :
    print(0)
    exit()
else :
    tomatoesRipen()

maxDay = 0
for i in range(H) :
    for j in range(N) :
        for k in range(M) :
            if box[i][j][k] == 0 :
                print(-1)
                exit()
            else :
                maxDay = max(maxDay, box[i][j][k])
print(maxDay - 1)
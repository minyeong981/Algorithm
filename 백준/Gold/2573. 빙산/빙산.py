import sys
from collections import deque

input = sys.stdin.readline

def iceMcnt(r, c): # 빙하 분리된 개수 세기
    q = deque()
    q.append((r, c))
    visited[r][c] = True
    remain_ice = 1
    while q:
        vr, vc = q.popleft()

        for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nr = vr + dr
            nc = vc + dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and iceM[nr][nc] != 0:
                q.append((nr, nc))
                remain_ice += 1
                visited[nr][nc] = True
    return remain_ice

N, M = map(int, input().split())
iceM = [list(map(int, input().split())) for _ in range(N)]

year = 0

while True:
    cnt = 0
    visited = [[False] * M for _ in range(N)]
    sea = [[0] * M for _ in range(N)]
    flag = False

    # 분리된 빙하 개수 세기
    for r in range(N):
        for c in range(M):
            if iceM[r][c] != 0 and not visited[r][c]:
                remain_ice = iceMcnt(r, c)
                cnt += 1
                if cnt >= 2:
                    flag = True
                    break
        if flag:
            break
    if flag:
        break

    # 다 녹을 때까지 한 덩어리면 0 출력
    melted_ice = 0
    for i in range(N):
        for j in range(M):
            if iceM[i][j] > 0:
                for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    nr = i + dr
                    nc = j + dc
                    if 0 <= nr < N and 0 <= nc < M and iceM[nr][nc] == 0:
                        sea[i][j] += 1

    for i in range(N):
        for j in range(M):
            if iceM[i][j] > 0:
                iceM[i][j] = max(0, iceM[i][j] - sea[i][j])
                if iceM[i][j] == 0:
                    melted_ice += 1

    if melted_ice == remain_ice:  # 다 녹은 빙산의 수와 남은 빙산의 수가 같으면
        year = 0
        break

    year += 1

print(year)

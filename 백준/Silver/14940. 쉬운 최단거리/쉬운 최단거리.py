from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # n: 세로(행), m: 가로(열)
mapLocation = [list(map(int, input().split())) for _ in range(n)]
countLocation = [[0] * m for _ in range(n)]

def findDistance(sr, sc):
    queue = deque([(sr, sc)])
    visited = [[0] * m for _ in range(n)]
    visited[sr][sc] = 1

    while queue:
        xr, xc = queue.popleft()
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:  # 하, 우, 상, 좌 이동
            nr = xr + dr
            nc = xc + dc
            if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == 0 and mapLocation[nr][nc] == 1:
                countLocation[nr][nc] = countLocation[xr][xc] + 1
                visited[nr][nc] = 1
                queue.append((nr, nc))

# 시작 위치(2)를 기준으로 BFS 실행
for r in range(n):
    for c in range(m):
        if mapLocation[r][c] == 2:
            findDistance(r, c)

# 도달할 수 없는 위치(1) 처리
for r in range(n):
    for c in range(m):
        if mapLocation[r][c] == 1 and countLocation[r][c] == 0:
            countLocation[r][c] = -1

# 결과 출력
for row in countLocation:
    print(*row)

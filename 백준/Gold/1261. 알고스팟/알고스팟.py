import heapq
import sys
input = sys.stdin.readline

def solve(r, c) :
    q = []
    heapq.heappush(q, (0, r, c))
    visited = [[float('inf')] * m for _ in range(n)]
    visited[r][c] = 0
    while q :
        w, x, y = heapq.heappop(q)

        if visited[x][y] < w :
            continue

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)] :
            nx, ny = x + dx, y +dy
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == float('inf') :
                if arr[nx][ny] == 0 :
                    visited[nx][ny] = visited[x][y]
                else :
                    visited[nx][ny] = visited[x][y] + 1
                heapq.heappush(q, (visited[nx][ny], nx, ny))

    return visited[n-1][m-1]

m, n = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]

print(solve(0, 0))
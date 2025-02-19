from collections import deque
import sys
input = sys.stdin.readline

def bfs(r, c, p) :
    q = deque()
    q.append((r, c))
    visited[r][c] = 1
    result = 1
    while q :
        x, y = q.popleft()

        for dr, dc in [(1,0), (0,1), (-1,0), (0,-1)] :
            nx = x + dr
            ny = y + dc
            if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == 0 and arr[nx][ny] == p:
                visited[nx][ny] = 1
                result += 1
                q.append((nx, ny))


    return result*result



N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(M)]
visited = [[0] * N for _ in range(M)]

B = 0
W = 0
for r in range(M) :
    for c in range(N) :
        if arr[r][c] == 'B' and  visited[r][c] == 0 :
            B += bfs(r,c,'B')
        elif arr[r][c] == 'W' and  visited[r][c] == 0 :
            W += bfs(r,c,'W')
print(W, B)
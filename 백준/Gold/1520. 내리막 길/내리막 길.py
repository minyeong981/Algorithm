import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def solve(r, c) :
    if (r, c) == (M - 1, N - 1):
        return 1

    if visited[r][c] >= 0 :
        return visited[r][c]

    visited[r][c] = 0 # 방문 처리

    for dr, dc in [(1, 0), (0, 1), (0, -1), (-1, 0)] :
        nr, nc = r + dr, c + dc
        if 0 <= nr < M and 0 <= nc < N and arr[nr][nc] < arr[r][c] :
            visited[r][c] += solve(nr, nc)

    return visited[r][c]

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
visited = [[-1] * N for _ in range(M)]

print(solve(0, 0))

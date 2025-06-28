import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 이동 방향 : 순서 무관
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]  # 현재 위치에서 이동 가능한 최대 칸 수 저장

def dfs(x, y) :
    if dp[x][y] :
        return dp[x][y]

    dp[x][y] = 1

    for dx, dy in directions :
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and forest[nx][ny] > forest[x][y] :
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)

    return dp[x][y]

result = 0
for r in range(n) :
    for c in range(n) :
        result = max(result, dfs(r, c))
print(result)

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(x, y, bitMask, count):
    global maxV
    if (x, y, bitMask) in visited:
        return
    visited.add((x, y, bitMask))

    maxV = max(maxV, count)
    if maxV == 26:
        return

    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C:
            alpha = ord(arr[nx][ny]) - ord('A')
            if not (bitMask & (1 << alpha)):
                dfs(nx, ny, bitMask | (1 << alpha), count + 1)

R, C = map(int, input().split())
arr = [list(input().strip()) for _ in range(R)]
visited = set()  # (x, y, bitMask) 조합 저장
maxV = 0
startAlpha = ord(arr[0][0]) - ord('A')
dfs(0, 0, 1 << startAlpha, 1)
print(maxV)

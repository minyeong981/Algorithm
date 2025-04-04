from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y, targetX, targetY) :
    q = deque()
    q.append((x, y))
    visited = [[0] * I for _ in range(I)]
    visited[x][y] = 0
    while q :
        cuX, cuY = q.popleft()

        if (cuX, cuY) == (targetX, targetY) :
            return visited[cuX][cuY]

        for dr, dc in [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (2, -1), (2, 1), (1, -2), (1, 2)] :
            newX = cuX + dr
            newY = cuY + dc
            if 0 <= newX < I and 0 <= newY < I and visited[newX][newY] == 0 :
                visited[newX][newY] = visited[cuX][cuY] + 1
                q.append((newX, newY))


t = int(input().strip())
for _ in range(t) :
    I = int(input().strip())
    currR, currC = map(int, input().split())
    moveR, moveC = map(int, input().split())
    print(bfs(currR, currC, moveR, moveC))
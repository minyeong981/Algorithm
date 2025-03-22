from collections import deque
import sys
input = sys.stdin.readline

# 유니온 파인드
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 섬 번호 부여
def findIsland(r, c, islandNum):
    q = deque()
    q.append((r, c))
    visitedIsland[r][c] = True
    maps[r][c] = islandNum
    while q:
        x, y = q.popleft()
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr, nc = x + dr, y + dc
            if 0 <= nr < N and 0 <= nc < M and not visitedIsland[nr][nc] and maps[nr][nc] == 1:
                visitedIsland[nr][nc] = True
                maps[nr][nc] = islandNum
                q.append((nr, nc))

# 다리 탐색
def canMove(startIsland, nr, dr, nc, dc):
    dist = 0
    while 0 <= nr < N and 0 <= nc < M:
        if maps[nr][nc] != 0:
            if maps[nr][nc] != startIsland and dist >= 2:
                return maps[nr][nc], dist
            else:
                return 0, 0
        nr += dr
        nc += dc
        dist += 1
    return 0, 0

def findEdges():
    for r in range(N):
        for c in range(M):
            if maps[r][c] > 0:
                islandNum = maps[r][c]
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < M and maps[nr][nc] == 0:
                        otherIsland, dist = canMove(islandNum, nr, dr, nc, dc)
                        if otherIsland != 0:
                            edgeList.append((dist, islandNum, otherIsland))

# 입력
N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

# 1. 섬 번호 부여
visitedIsland = [[False] * M for _ in range(N)]
islandNum = 1
for r in range(N):
    for c in range(M):
        if not visitedIsland[r][c] and maps[r][c] == 1:
            findIsland(r, c, islandNum)
            islandNum += 1

# 2. 간선 탐색 및 저장
edgeList = []
findEdges()

# 3. 크루스칼 알고리즘
edgeList.sort(key=lambda x: x[0])  # 비용 순 정렬
parent = [i for i in range(islandNum)]

result = 0
connected = 0

for dist, a, b in edgeList:
    if find(a) != find(b):
        union(a, b)
        result += dist
        connected += 1

# 4. 모든 섬 연결 확인 (섬 개수 - 1개 간선이어야 연결 완료)
if connected == islandNum - 2:  # islandNum-1 번째까지 증가했으므로 -2
    print(result)
else:
    print(-1)

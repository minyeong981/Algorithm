from collections import deque

def bfs(r,c):
    q = deque()
    q.append((r,c))
    painting_s = 1
    painting[r][c] = 0
    while q :
        vr, vc = q.popleft()
        for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
            nr = vr + dr
            nc = vc + dc
            if 0 <= nr < m and 0 <= nc < n and painting[nr][nc] == 1 :
                q.append((nr, nc))
                painting_s += 1
                painting[nr][nc] = 0
    return painting_s



m, n = map(int, input().split())
painting = [list(map(int, input().split())) for _ in range(m)]

cnt = 0
S = []
for row in range(m) :
    for col in range(n) :
        if painting[row][col] == 1 :
            S.append(bfs(row, col))
            cnt += 1

if S :
    print(len(S))
    print(max(S))
else :
    print(0)
    print(0)
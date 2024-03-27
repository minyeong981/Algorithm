from collections import deque

def bfs():
    q = deque()
    q.append((0,0))
    visited[0][0] = True
    cnt = 0
    while q :
        vr, vc = q.popleft()
        for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
            nr = vr + dr
            nc = vc + dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] :
                if cheese[nr][nc] == 0 :
                    visited[nr][nc] = True
                    q.append((nr, nc))
                elif cheese[nr][nc] == 1:
                    cheese[nr][nc] = 0
                    visited[nr][nc] = True
                    cnt += 1
    cheeselst.append(cnt)
    return cnt

N, M = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(N)]

day = 0
cheeselst = []
while True :
    visited = [[False]*M for _ in range(N)]
    cnt = bfs()
    if cnt == 0 :
        break
    day += 1
print(day)
print(cheeselst[-2])

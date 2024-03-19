from collections import deque

def bfs(r, c) :
    q = deque()
    q.append((r,c))
    island_map[r][c] = 0
    while q :
        vr, vc = q.popleft()

        for dr, dc in [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
            nr = vr + dr
            nc = vc + dc
            if 0 <= nr < h and 0 <= nc < w and island_map[nr][nc] == 1 :
                q.append((nr,nc))
                island_map[nr][nc] = 0

while True :
    w, h = map(int, input().split())
    if w == 0 and h == 0 :
        break
    island_map = [list(map(int, input().split())) for _ in range(h)]

    cnt = 0
    for row in range(h):
        for col in range(w):
            if island_map[row][col] == 1 :
                bfs(row, col)
                cnt += 1
    print(cnt)
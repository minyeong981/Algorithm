from collections import deque

def bfs():
    global cnt
    while q:
        # 현재 위치에서 물 이동
        for _ in range(len(water_q)):
            wr, wc = water_q.popleft()
            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nr = wr + dr
                nc = wc + dc
                if 0 <= nr < r and 0 <= nc < c and (MAP[nr][nc] == '.' or MAP[nr][nc] == 'S'):
                    MAP[nr][nc] = '*'
                    water_q.append((nr, nc))

        # 현재 위치에서 고슴도치 이동
        for _ in range(len(q)):
            qr, qc = q.popleft()
            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nr = qr + dr
                nc = qc + dc
                if 0 <= nr < r and 0 <= nc < c:
                    if MAP[nr][nc] == '.':
                        q.append((nr, nc))
                        MAP[nr][nc] = 'S'
                    elif MAP[nr][nc] == 'D':
                        print(cnt + 1)
                        return
        cnt += 1
    print("KAKTUS")
    return


r, c = map(int, input().split())
MAP = [list(input().strip()) for _ in range(r)]

water_q = deque()
q = deque()

for i in range(r):
    for j in range(c):
        if MAP[i][j] == '*':
            water_q.append((i, j))
        elif MAP[i][j] == 'S':
            q.append((i, j))

cnt = 0
bfs()
from collections import deque

def bfs(r,c) :
    q = deque()
    q.append((r,c))
    arr[r][c] = 1
    value = 1
    while q :
        vr, vc = q.popleft()
        for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
            nr = vr + dr
            nc = vc + dc
            if 0 <= nr < M and 0 <= nc < N and arr[nr][nc] == 0:
                q.append((nr, nc))
                # arr[nr][nc] = arr[vr][vc] + 1
                arr[nr][nc] = 1
                value += 1
    return value


M, N, K = map(int, input().split())
arr = [[0]*N for _ in range(M)]
for _ in range(K) :
    x1, y1, x2, y2 = map(int, input().split())

    for j in range(x1, x2) :
        for i in range(y1, y2) :
            arr[i][j] = 1
cnt = 0
S = []
for r in range(M) :
    for c in range(N) :
        if arr[r][c] == 0 :
            S.append(bfs(r,c))
            cnt += 1

S.sort()
print(cnt)
print(*S)

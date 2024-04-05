from collections import deque

def bfs(i, j, dis):
    disQ = deque([(i, j, dis)])
    visited = [[False] * c for _ in range(r)]
    visited[i][j] = True  # 초기 방문 표시
    while disQ :
        vr, vc, dis = disQ.popleft()
        for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
            nr = vr + dr
            nc = vc + dc
            if 0 <= nr < r and 0 <= nc < c and not visited[nr][nc] and MAP[nr][nc] == 'L':
                disQ.append((nr,nc, dis+1))
                visited[nr][nc] = True

    return dis


r, c = map(int, input().split())
MAP = [list(input()) for _ in range(r)]

result = 0
for i in range(r):
    for j in range(c):
        if MAP[i][j] == 'L' :
            result = max(result, bfs(i,j, 0))  # 각 육지에 대해 최단 거리를 구하고 최대 값을 갱신

print(result)

# 문어박사님st

from collections import deque
def bfs(r, c):
    q = deque()
    q.append((r,c))
    visited = [[0]*N for _ in range(N)]
    visited[r][c] = 1
    lst = []
    eat = 0

    while q :
        vr, vc = q.popleft()
        if eat == visited[vr][vc] :
            return lst, eat-1

        for dr, dc in [(-1,0),(0,-1),(1,0),(0,1)]:
            nr = vr + dr
            nc = vc + dc
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and arr[nr][nc] <= shark :
                q.append((nr,nc))
                visited[nr][nc] = visited[vr][vc] + 1
                if 0 < arr[nr][nc] < shark :
                    lst.append((nr,nc))
                    eat = visited[nr][nc]
    return lst, eat-1  # 엄마에게 요청



N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 9 :
            row, col = i, j
            arr[i][j] = 0


shark = 2
cnt = ans = 0
while True :
    lst, dist = bfs(row,col) # 가장 가까운 거리
    if len(lst) == 0: # 더 이상 먹을 물고기 없다면
        break
    lst.sort(key = lambda x:(x[0],x[1])) # 행,열 순서대로 정렬
    row, col = lst[0] # 가장 위쪽에 있는
    arr[row][col] = 0 # 물고기 먹기
    cnt += 1
    ans += dist
    if shark == cnt : #크기만큼 물고기 먹은 경우
        shark += 1    #크기 +1
        cnt = 0

print(ans)

from collections import deque

def bfs(r,c, cnt):
    q = deque()
    q.append((r,c))
    visited[r][c] = True
    while q :
        vr, vc = q.popleft()
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)] :
            nr = vr + dr
            nc = vc + dc
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] :
                if arr[nr][nc] == 1 :
                    q.append((nr, nc))
                    visited[nr][nc] = True
                    cnt +=1
                    # print(cnt)
                else :
                    visited[nr][nc] = True
    return cnt


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
cnt = 1
cntlst = []
for row in range(N) :
    for col in range(N) :
        if arr[row][col] == 1 and not visited[row][col]:
            cntlst.append(bfs(row,col,cnt))

print(len(cntlst))
cntlst.sort()
for i in range(len(cntlst)):
    print(cntlst[i])
from collections import deque
import copy

def virus_bfs():
    global maxV
    labCopy = copy.deepcopy(lab) # 함수 돌 때 마다 초기화
    virus = deque()

    # 바이러스 위치 다 담아놓기
    for r in range(N):
        for c in range(M):
            if lab[r][c] == 2:
                virus.append((r, c))

    while virus :
        vr, vc = virus.popleft()

        for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
            nr = vr + dr
            nc = vc + dc
            if 0 <= nr < N and 0 <= nc < M and labCopy[nr][nc] == 0 :
                labCopy[nr][nc] = 2
                virus.append((nr,nc))

    # 0인 곳 안전영역
    safetyZone = 0
    for i in labCopy :
        safetyZone += i.count(0)
    maxV = max(maxV, safetyZone)

def dfs(cnt):
    # 기저 조건
    if cnt == 3 : # 벽 다 세우면
        virus_bfs() # 바이러스 확산 시키기
        return

    # 벽을 세울 수 있는 경우의 수 구하기(조합)
    for r in range(N) :
        for c in range(M) :
            if lab[r][c] == 0 :
                lab[r][c] = 1
                dfs(cnt+1)
                lab[r][c] = 0


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
maxV = 0
dfs(0)

print(maxV)
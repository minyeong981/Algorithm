import copy

def cctv(arr, k):
    global minV

    if k == len(cctvLst):
        minV = min(minV, noCntArea(arr)) # 사각지대 최솟값 구하기
        return
    else :
        arrCopy = copy.deepcopy(arr) # 딥 카피 하는 법
        cctvType, r, c = cctvLst[k]
        for dir in cctvD[cctvType]:
            watch(r, c, dir, arrCopy) # 감시 영역 호출
            cctv(arrCopy, k+1)
            arrCopy = copy.deepcopy(arr) # 다른 방향 회전 후 재탐색 위해


def watch(r, c, dir, arrCopy) :
    for d in dir :
        nr = r
        nc = c

        while True :    # 탐색
            nr += directions[d][0]
            nc += directions[d][1]
            if 0 <= nr < n and 0 <= nc < m :
                if arrCopy[nr][nc] == 6 : # 벽이면
                    break
                elif arrCopy[nr][nc] == 0 :
                    arrCopy[nr][nc] = '#'
            else :
                break


def noCntArea(arr) :
    cnt = 0

    for i in range(n) :
        for j in range(m) :
            if arr[i][j] == 0 :
                cnt += 1
    return cnt




n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

cctvLst = []

for r in range(n):
    for c in range(m):
        if arr[r][c] > 0 and arr[r][c] < 6:
            cctvLst.append((arr[r][c], r, c))  # cctv 번호, 행, 열 넣기

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 시계 방향, 상, 우, 하, 좌
cctvD = [
        [],
        [[0], [1], [2], [3]], # 1번 방향
        [[0, 2], [1, 3]],     # 2번 방향
        [[0, 1], [0, 3], [1, 2], [2, 3]], # 3번 방향
        [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]], # 4번 방향
        [[0, 1, 2, 3]] # 5번 방향
        ]

minV = float('inf')
cctv(arr, 0)
print(minV)
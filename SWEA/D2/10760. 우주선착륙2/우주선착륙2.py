T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for row in range(N):
        for col in range(M):
            lst = []
            for dr, dc in [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)] :
                nR = row + dr
                nC = col + dc
                if 0 <= nR < N and 0 <= nC < M :
                    if arr[row][col] > arr[nR][nC] :
                        lst.append(arr[nR][nC])
            if len(lst) > 3 :
                cnt += 1
    print(f'#{tc} {cnt}')
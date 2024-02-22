def bfs(ground, row, col) :
    q = []
    q.append((row, col))
    ground[row][col] = 0
    while q :
        vr, vc = q.pop(0)

        for dr, dc in [(1,0), (0,1), (-1,0), (0,-1)] :
            newR = vr + dr
            newC = vc + dc
            if 0 <= newR < N and 0 <= newC < M and ground[newR][newC] == 1 :
                ground[newR][newC] = 0
                q.append((newR, newC))
    return

T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())
    ground = [[0]*M for _ in range(N)]
    cnt = 0

    for _ in range(K) :
        X, Y = map(int, input().split())
        ground[Y][X] = 1
    for row in range(N) :
        for col in range(M) :
            if ground[row][col] == 1 :
                bfs(ground, row, col)
                cnt += 1
    print(cnt)
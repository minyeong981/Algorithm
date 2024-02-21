def bfs(row, col, cnt) :
    q = []
    visited = [[False]*M for _ in range(N)]
    q.append((row, col, 1))
    visited[row][col] = True

    while q :
        vr, vc, cnt = q.pop(0)
        if (vr,vc) == (N-1,M-1):
            return cnt
        for dr, dc in [(1,0), (-1,0), (0,1), (0, -1)] :
            newR = vr + dr
            newC = vc + dc
            if 0<=newR <N and 0 <= newC < M and not visited[newR][newC] and maze[newR][newC] != '0' :
                q.append((newR, newC, cnt+1))
                visited[newR][newC] = True

    return -1

N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]
result = bfs(0,0, 0)
print(result)
from collections import deque
def solution(maps):
    
    # n, m
    n = len(maps)
    m = len(maps[0])
        
    q = deque([(0, 0)])
    visited = [[-1] * m for _ in range(n)]
    visited[0][0] = 1
    while q :
        r, c = q.popleft()
        
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)] :
            nr, nc = dr + r, dc + c
            if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == -1 and maps[nr][nc] :
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc))
    
    return visited[n - 1][m - 1]
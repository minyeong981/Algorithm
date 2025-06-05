from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[0]*102 for _ in range(102)]

    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1*2, y1*2, x2*2, y2*2
        for i in range(x1, x2+1) :
            for j in range(y1, y2+1) :
                board[i][j] = 1

    for x1, y1, x2, y2 in rectangle :
        x1, y1, x2, y2 = x1*2, y1*2, x2*2, y2*2
        for i in range(x1+1, x2):
            for j in range(y1+1, y2) :
                board[i][j] = 0

    q = deque()
    visited = [[0]*102 for _ in range(102)]
    q.append((characterX*2, characterY*2))
    visited[characterX*2][characterY*2] = 1

    while q:
        x, y = q.popleft()
        if (x, y) == (itemX*2, itemY*2):
            return (visited[x][y]-1)//2
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)] :
            nx, ny = x+dx, y+dy
            if board[nx][ny] and not visited[nx][ny] :
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

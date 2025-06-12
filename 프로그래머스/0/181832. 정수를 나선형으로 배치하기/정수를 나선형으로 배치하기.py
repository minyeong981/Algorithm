def solution(n):
    arr = [[0] * n for _ in range(n)]
    r = c = 0
    arr[r][c] = 1
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    index = 0
    for count in range(2, n*n+1) :
        for _ in range(4) :
            nr, nc = r + dr[index], c + dc[index]
            if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == 0 :
                arr[nr][nc] = count
                r,c = nr, nc
                break
            index = (index + 1) % 4
    return arr
M, N = map(int, input().split())
arr = [[0]*N for _ in range(M)]

#우,하,좌,상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
d = 0
cnt = 0
v = 0
row, col = 0, 0
while v <M*N:
    v += 1
    arr[row][col] = v
    newR = row + dr[d]
    newC = col + dc[d]
    if 0 > newR or newR >= M or 0 > newC or newC >= N or arr[newR][newC] != 0 :
        d = (d+1)%4
        cnt += 1
    row = row + dr[d]
    col = col + dc[d]

print(cnt-1)
N, M = map(int, input().split())
r, c, d = map(int, input().split()) #로봇 청소기 현재 위치 / 0 북, 1 동, 2 남, 3 서
room = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def clean(r, c, d):
    global cnt

    # 조건 1
    if room[r][c] == 0:
        room[r][c] = 2  # 청소했으면 2
        cnt += 1

    # 조건 3
    for _ in range(4):
        nd = (d + 3) % 4  # 반시계 방향
        nr = r + dr[nd]
        nc = c + dc[nd]

        if 0 <= nr < N and 0 <= nc < M and room[nr][nc] == 0:
            clean(nr, nc, nd) # 조건 1로 돌아가기
            return            # 이후 코드는 실행하지 않음
        else :
            d = nd # 방향만 설정해놓기


    # 조건 2 : 네 방향 모두 청소할 곳이 없는 경우
    nd = (d + 2) % 4  # 후진 방향
    nr = r + dr[nd]
    nc = c + dc[nd]
    if 0 <= nr < N and 0 <= nc < M and room[nr][nc] != 1:
        clean(nr, nc, d)

cnt = 0
clean(r, c, d)
print(cnt)
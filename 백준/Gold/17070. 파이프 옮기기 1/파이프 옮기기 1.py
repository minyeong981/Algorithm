import sys
input = sys.stdin.readline


def dfs(r, c, dir):
    global cnt

    if r == N-1 and c == N-1:
        cnt += 1
        return

    # 파이프가 가로면
    if dir == 0:
        if c+1 < N and arr[r][c+1] == 0:  # 오른쪽
            dfs(r, c+1, 0)
        if r+1 < N and c+1 < N and arr[r+1][c] == 0 and arr[r][c+1] == 0 and arr[r+1][c+1] == 0:  # 대각선
            dfs(r+1, c+1, 2)

    # 파이프가 세로면
    elif dir == 1:
        if r+1 < N and arr[r+1][c] == 0:  # 아래
            dfs(r+1, c, 1)
        if r+1 < N and c+1 < N and arr[r+1][c] == 0 and arr[r][c+1] == 0 and arr[r+1][c+1] == 0:  # 대각선
            dfs(r+1, c+1, 2)

    # 파이프가 대각선이면
    elif dir == 2:
        if c+1 < N and arr[r][c+1] == 0:  # 오른쪽
            dfs(r, c+1, 0)
        if r+1 < N and arr[r+1][c] == 0:  # 아래
            dfs(r+1, c, 1)
        if r+1 < N and c+1 < N and arr[r+1][c] == 0 and arr[r][c+1] == 0 and arr[r+1][c+1] == 0:  # 대각선
            dfs(r+1, c+1, 2)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
dfs(0, 1, 0)  # 파이프 위치 (0, 1), 시작 방향 가로

print(cnt)
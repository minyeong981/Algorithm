import sys
input = sys.stdin.readline

# 8방향 이동 (상, 하, 좌, 우, 대각선)
directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),          (0, 1),
              (1, -1), (1, 0), (1, 1)]

# 최종 목적지를 찾는 함수 (경로 압축 적용)
def find_sink(x, y):
    # 이미 sink 값이 설정되어 있으면 그대로 반환
    if sink[x][y] != (-1, -1):
        return sink[x][y]

    min_value = board[x][y]
    target = (x, y)

    # 8방향 탐색
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C:
            if board[nx][ny] < min_value:
                min_value = board[nx][ny]
                target = (nx, ny)

    # 이동할 곳이 있다면 재귀적으로 최종 목적지 찾기
    if target != (x, y):
        sink[x][y] = find_sink(*target)
    else:
        sink[x][y] = (x, y)

    return sink[x][y]

# 입력 받기
R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

# 각 칸의 최종 목적지를 기록할 배열
sink = [[(-1, -1) for _ in range(C)] for _ in range(R)]
# 각 칸에 최종적으로 몇 개의 공이 도달하는지 기록
result = [[0] * C for _ in range(R)]

# 각 칸에서 시작하여 최종 목적지 찾기
for i in range(R):
    for j in range(C):
        final_x, final_y = find_sink(i, j)
        result[final_x][final_y] += 1

# 결과 출력
for row in result:
    print(*row)

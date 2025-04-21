import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

r, c, n = map(int, input().split())
arr = [list(input().strip()) for _ in range(r)]

# 폭탄 설치 시간을 기록할 배열
bomb_time = [[-1] * c for _ in range(r)]

# 초기 폭탄은 0초에 설치된 것으로 간주
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'O':
            bomb_time[i][j] = 0

# 폭발 처리
def explode(time):
    to_explode = []
    for i in range(r):
        for j in range(c):
            if bomb_time[i][j] != -1 and time - bomb_time[i][j] == 3:
                to_explode.append((i, j))

    for x, y in to_explode:
        arr[x][y] = '.'
        bomb_time[x][y] = -1
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c:
                if bomb_time[nx][ny] != -1 and time - bomb_time[nx][ny] != 3:
                    arr[nx][ny] = '.'
                    bomb_time[nx][ny] = -1

# 폭탄 설치
def install(time):
    for i in range(r):
        for j in range(c):
            if arr[i][j] == '.':
                arr[i][j] = 'O'
                bomb_time[i][j] = time


def simulate(time):
    if time > n:
        return

    if time % 2 == 0:
        install(time)
    else:
        explode(time)

    simulate(time + 1)

simulate(1)

for row in arr:
    print(''.join(row))

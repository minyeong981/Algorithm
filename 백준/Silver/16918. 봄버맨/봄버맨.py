import sys
input = sys.stdin.readline

r, c, n = map(int, input().split())
arr = [list(input().strip()) for _ in range(r)]

# 폭탄이 터진 후 상태 계산 함수
def explode(arr):
    result = [['O'] * c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if arr[x][y] == 'O':
                result[x][y] = '.'
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < r and 0 <= ny < c:
                        result[nx][ny] = '.'
    return result

if n == 1:
    for row in arr:
        print(''.join(row))
elif n % 2 == 0:
    for _ in range(r):
        print('O' * c)
else:
    after1 = explode(arr)
    after2 = explode(after1)

    result = after1 if n % 4 == 3 else after2
    for row in result:
        print(''.join(row))
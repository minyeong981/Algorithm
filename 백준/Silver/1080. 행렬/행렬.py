import sys
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
A = [list(map(int, input().strip())) for _ in range(N)]
B = [list(map(int, input().strip())) for _ in range(N)]

cnt = 0

# 3x3 행렬에서 원소 뒤집는 함수
def changeEle(i, j, arr):
    for r in range(i, i+3):
        for c in range(j, j+3):
            arr[r][c] = 1 - arr[r][c]

# A와 B를 비교하면서 차이가 나는 위치에서 뒤집기 수행
for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            changeEle(i, j, A)
            cnt += 1

# A와 B 비교하여 일치 여부 확인
if A != B:
    cnt = -1

print(cnt)

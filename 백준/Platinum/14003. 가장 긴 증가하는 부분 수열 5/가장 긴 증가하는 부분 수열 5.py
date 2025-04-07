import bisect
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

temp = [A[0]]         # LIS 배열 (실제 값 저장)
pos = [0] * N         # A[i]가 LIS의 몇 번째 값에 해당하는지 저장
prev = [-1] * N       # 이전 값의 인덱스를 저장해 복원용으로 사용

lis_idx = [0]         # LIS 마지막에 해당하는 A의 인덱스를 저장

for i in range(1, N):
    if A[i] > temp[-1]:
        prev[i] = lis_idx[-1]  # 이전 인덱스 기록
        temp.append(A[i])
        pos[i] = len(temp) - 1
        lis_idx.append(i)
    else:
        idx = bisect.bisect_left(temp, A[i])
        temp[idx] = A[i]
        pos[i] = idx
        if idx > 0:
            prev[i] = lis_idx[idx - 1]
        lis_idx[idx] = i  # 해당 위치를 지금 인덱스로 업데이트

# LIS 복원
result = []
cur = lis_idx[-1]
while cur != -1:
    result.append(A[cur])
    cur = prev[cur]

result.reverse()
print(len(result))
print(*result)

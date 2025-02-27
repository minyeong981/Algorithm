import sys
input = sys.stdin.readline

N = int(input().strip())
k = int(input().strip())

s = 1
e = N * N
while s <= e :
    mid = (s + e) // 2
    cnt = sum(min(mid // row, N) for row in range(1, N + 1))
    if cnt < k :
        s = mid + 1
    else :
        e = mid - 1
print(s)
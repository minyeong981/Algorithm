import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lineList = [int(input()) for _ in range(k)]

s = 1
e = max(lineList)
result = 0

while s <= e :
    mid = (s + e) // 2 # 중앙값
    cnt = sum(line // mid for line in lineList)

    if cnt < n : # 랜선 개수가 n 보다 작으면
        e = mid - 1 # 더 짧은 길이로
    else :
        result = mid # 가능한 길이 중 최댓값
        s = mid + 1 # 더 긴 길이로
print(result)
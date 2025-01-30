import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mList = list(map(int, input().split()))
cList = list(map(int, input().split()))
mcList = list(zip(mList, cList))

maxM = sum(mList)
dp = [float('inf')]*(maxM + 1)
dp[0] = 0

for m, c in mcList :
    for j in range(maxM, m - 1, -1) :
        dp[j] = min(dp[j], dp[j - m] + c)
print(min(dp[M:maxM + 1]))
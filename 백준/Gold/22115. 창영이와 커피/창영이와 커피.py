import sys
input = sys.stdin.readline

N, K = map(int, input().split())
caffeine = list(map(int, input().split()))

dp = [float('inf')] * (K + 1)
dp[0] = 0

for c in caffeine:
    for i in range(K, c - 1, -1):
        dp[i] = min(dp[i], dp[i - c] + 1)

if dp[K] == float('inf'):
    print(-1)
else:
    print(dp[K])
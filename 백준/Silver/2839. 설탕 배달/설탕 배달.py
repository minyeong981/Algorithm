import sys

N = int(sys.stdin.readline().strip())
dp = [float('inf')] * (N + 1)
dp[0] = 0  # 0kg을 만들기 위한 최소 봉지 수는 0

for i in range(N + 1):
    if dp[i] == float('inf'):
        continue
    if i + 3 <= N:
        dp[i + 3] = min(dp[i + 3], dp[i] + 1)
    if i + 5 <= N:
        dp[i + 5] = min(dp[i + 5], dp[i] + 1)

print(dp[N] if dp[N] != float('inf') else -1)

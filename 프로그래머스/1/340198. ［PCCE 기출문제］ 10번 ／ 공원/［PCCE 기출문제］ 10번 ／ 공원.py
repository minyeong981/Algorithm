def solution(mats, park):
    n, m = len(park), len(park[0])
    matsSet = set(mats)
    dp = [[0] * m for _ in range(n)]
    maxSizes = set()

    for i in range(n):
        for j in range(m):
            if park[i][j] == '-1':
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                if dp[i][j] in matsSet:
                    maxSizes.add(dp[i][j])

    return max(maxSizes) if maxSizes else -1

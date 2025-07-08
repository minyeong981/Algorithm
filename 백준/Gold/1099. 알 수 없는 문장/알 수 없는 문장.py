string = input()
string_length = len(string)
n = int(input())
patterns = []
min_length = float('inf')

for _ in range(n) :
    char = input()
    patterns.append(char)
    min_length = min(min_length, len(char))

dp = [float('inf')] * (string_length+1)
dp[0] = 0

for i in range(string_length) :
    for j in range(i + min_length, string_length + 1) :
        substr = string[i:j]
        for pattern in patterns :
            if len(pattern) != len(substr) : continue
            if sorted(pattern) == sorted(substr) :
                price = sum(1 for c1, c2 in zip(pattern, substr) if c1 != c2)
                dp[j] = min(dp[j], dp[i] + price)

if dp[string_length] == float('inf') :
    print(-1)
else :
    print(dp[string_length])
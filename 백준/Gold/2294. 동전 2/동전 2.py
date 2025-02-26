import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coin = set()
for _ in range(n) :
    x = int(input().strip())
    if x > k :
        continue
    coin.add(x)

INF = float('inf')
cntDp = [INF] * (k + 1)
cntDp[0] = 0

for c in coin :
    for i in range(c, k + 1) :
        cntDp[i] = min(cntDp[i], cntDp[i - c] + 1)

if cntDp[k] != INF :
    print(cntDp[k])
else :
    print(-1)

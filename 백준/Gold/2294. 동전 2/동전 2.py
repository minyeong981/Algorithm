import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coinLst = []
for _ in range(n) :
    coinLst.append(int(input().strip()))
coinLst.sort()
INF = float('inf')
cntDp = [INF] * (k + 1)
cntDp[0] = 0

for c in coinLst :
    for i in range(c, k + 1) :
        cntDp[i] = min(cntDp[i], cntDp[i - c] + 1)

if cntDp[k] != INF :
    print(cntDp[k])
else :
    print(-1)
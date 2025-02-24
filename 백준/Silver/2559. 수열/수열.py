import sys
input = sys.stdin.readline

N, K = map(int, input().split())
tem = list(map(int, input().split()))
maxV = -float('inf')
s = -1
e = K - 1
sumTem = sum(tem[: K])
while e < N :
    if maxV < sumTem :
        maxV = sumTem
    if e == N -1 :
        break
    s += 1
    e += 1
    sumTem = sumTem - tem[s] + tem[e]

print(maxV)
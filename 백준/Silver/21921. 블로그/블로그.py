import sys
input = sys.stdin.readline

N,K = map(int, input().split())
visited = list(map(int, input().split()))

maxV = sumV = sum(visited[:K])
cnt = 1
for i in range(1, N - K + 1) :
    sumV = sumV - visited[i - 1] + visited[i + K - 1]

    if maxV < sumV :
        maxV = sumV
        cnt = 1
    elif maxV == sumV :
        cnt += 1

if maxV == 0 :
    print('SAD')
else :
    print(maxV)
    print(cnt)
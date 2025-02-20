import sys
input = sys.stdin.readline

N = int(input().strip())
G = [list(map(int, input().split())) for _ in range(N)]

for k in range(N) :
    for i in range(N) :
        for j in range(N) :
            if G[i][k] == 1 and G[k][j] == 1 :
                G[i][j] = 1
for row in G :
    print(*row)
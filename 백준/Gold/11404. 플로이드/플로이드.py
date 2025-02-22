import sys
input = sys.stdin.readline

def solve(G) :
    for k in range(1, n + 1) :
        for i in range(1, n + 1) :
            for j in range(1, n + 1) :
                if i == j:
                    G[i][j] = 0
                elif G[i][k] != INF and G[k][j] != INF : # 가는 길이 있을 때
                    G[i][j] = min(G[i][j], G[i][k] + G[k][j])
                elif G[i][k] != INF and G[k][j] == INF : # 출발지부터 중간 지점까지만 갈 수 있을 때
                    G[i][k] = G[i][k]
                elif G[i][k] == INF and G[k][j] != INF : # 중간 지점에서 도착지까지만 갈 수 있을 때
                    G[k][j] = G[k][j]

    for r in range(1, n + 1) :
        for c in range(1, n + 1) :
            if G[r][c] == INF :
                G[r][c] = 0
    return G

n = int(input().strip())
m = int(input().strip())
INF = float('inf')
G = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m) :
    a, b, c = map(int, input().split())
    if G[a][b] == INF :
        G[a][b] = c
    else :
        if G[a][b] > c :
            G[a][b] = c
for row in solve(G)[1:] :
    print(*row[1:])

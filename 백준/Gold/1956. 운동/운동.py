import sys
input = sys.stdin.readline

def solve() :
    result = INF
    for k in range(1, V+1) :
        for i in range(1, V+1) :
            for j in range(1, V+1) :
                if G[i][k] != INF and G[k][j] != INF :
                    G[i][j] = min(G[i][j], G[i][k] + G[k][j])
                    result = min(result, G[i][j] + G[j][i])

    if result != INF :
        return result

    return -1

V, E = map(int, input().split())
INF = float('inf')
G = [[INF]*(V + 1) for _ in range(V + 1)]
for _ in range(E) :
    a, b, c = map(int, input().split())
    G[a][b] = c

print(solve())
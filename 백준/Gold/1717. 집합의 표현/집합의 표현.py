import sys
input = sys.stdin.readline

def find(parent, v):
    if parent[v] != v :
        parent[v] = find(parent, parent[v])
    return parent[v]

def union(parent, rank, x, y) :
    rootX = find(parent, x)
    rootY = find(parent, y)

    if rootX != rootY :
        if rank[rootX] > rank[rootY] :
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY] :
            parent[rootX] = rootY
        else :
            parent[rootX] = rootY
            rank[rootY] += 1

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
rank = [0] * (n + 1)
for _ in range(m) :
    q, a, b = map(int, input().split())
    if q == 0 :
        union(parent, rank, a, b)
    else :
        if find(parent, a) == find(parent, b) :
            print('YES')
        else :
            print('NO')
import sys
input = sys.stdin.readline

def find(parent, x) :
    if parent[x] != x :
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, a, b) :
    rootA = find(parent, a)
    rootB = find(parent, b)

    if rootA != rootB :
        if rank[rootA] > rank[rootB] :
            parent[rootB] = rootA
        elif rank[rootA] < rank[rootB] :
            parent[rootA] = rootB
        else :
            parent[rootB] = rootA
            rank[rootA] += 1
        return True
    return False


def kruskal(m, edges) :
    parent = [i for i in range(m + 1)]
    rank = [0] * (m + 1)

    edges.sort(key=lambda x : x[2]) # 가중치 기준 정렬
    mstV = 0
    totalV = sum(w for _, _, w in edges)
    edgeV = 0

    for u, v, w in edges :
        if union(parent, rank, u, v) :
            mstV += w
            edgeV += 1
            if edgeV == m - 1 :
                break

    return totalV - mstV


while True :
    m, n = map(int, input().split())
    if m + n == 0 :
        break

    edges = []
    for _ in range(n) :
        x, y, z = map(int, input().split())
        edges.append((x, y, z))

    print(kruskal(m, edges))
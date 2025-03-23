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
            parent[rootA] = rootB
            rank[rootB] += 1
        return True

    return False


def solve() :
    parent = [i for i in range(V + 1)]
    rank = [0] * (V + 1)

    edges.sort(key= lambda x : x[2])
    mstV = 0
    edgeCnt = 0

    for a, b, c in edges :
        if union(parent, rank, a, b) :
            mstV += c
            edgeCnt += 1

            if edgeCnt == E :
                break

    return mstV

V, E = map(int, input().split())
edges = []

for _ in range(E) :
    A, B, C = map(int, input().split())
    edges.append((A, B, C))

print(solve())
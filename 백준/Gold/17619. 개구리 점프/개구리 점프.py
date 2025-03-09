import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def makeRoot(parent, root1, root2) :
    while root1 <= root2 :
        parent[root1] = root2
        root1 += 1

def find(parent, x) :
    if parent[x] != x :
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, level, x1, x2) :
    rootA = find(parent, x1)
    rootB = find(parent, x2)

    if rootA != rootB :
        if rootA > rootB :
            makeRoot(parent, rootB, rootA)
        elif rootA < rootB :
            makeRoot(parent, rootA, rootB)

def solve(pos, o1, o2) :
    pos.sort(key= lambda x : x[2], reverse=True)
    maxV = pos[0][2]

    parent = [i for i in range(maxV + 1)]
    level = [0] * (maxV + 1)

    for n, x1, x2, y in pos :
        union(parent, level, x1, x2)

    pos.sort(key= lambda x : x[0])
    if parent[pos[o1-1][1]] == parent[pos[o2-1][1]] :
        return 1
    return 0


N, Q = map(int, input().split())
pos = []

for i in range(1, N + 1) :
    x1, x2, y = map(int, input().split())
    pos.append((i, x1, x2, y))
for _ in range(Q) :
    o1, o2 = map(int, input().split())
    print(solve(pos, o1, o2))
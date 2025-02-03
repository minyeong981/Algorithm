import sys
input = sys.stdin.readline

def dfs(root, pList) :
    stack = [root]
    visited = [False] * (N + 1)
    visited[root] = True

    while stack :
        nodeP = stack.pop()

        for nodeC in G[nodeP] :
            if not visited[nodeC] :
                visited[nodeC] = True
                pList[nodeC] = nodeP
                stack.append(nodeC)

N = int(input())
G = [[] for _ in range(N + 1)]
visited = [False]*(N + 1)
pList = [0]*(N + 1)

for _ in range(N - 1) :
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

dfs(1, pList)

for p in pList[2:] :
    print(p)
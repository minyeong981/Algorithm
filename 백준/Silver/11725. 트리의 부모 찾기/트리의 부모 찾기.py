from collections import deque

def build_tree(root):
    q = deque()
    q.append(root)
    visited = [False] * (N + 1)
    visited[root] = True

    while q:
        v = q.popleft()
        for w in G[v]:
            if not visited[w]:
                tree[w] = v
                q.append(w)
                visited[w] = True
    # print(tree)

N = int(input())
G = [[] for _ in range(N + 1)]
tree = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

build_tree(1)

for i in range(2, N + 1):
    print(tree[i])
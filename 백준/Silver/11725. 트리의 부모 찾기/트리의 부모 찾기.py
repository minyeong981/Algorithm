def dfs(root) :
    st = []
    st.append(root)
    visited = [False] * (N+1)
    visited[root] = True

    while st :
        v = st.pop()

        for w in G[v]:
            if not visited[w] :
                st.append(w)
                tree[w] = v
                visited[w] = True



N = int(input())

G = [[] for _ in range(N+1)]
tree = [0] * (N+1)
# TREE = [[] for _ in range(N+1)]
for _ in range(N-1) :
    v1, v2 = map(int, input().split())
    G[v1].append(v2)
    G[v2].append(v1)
#print(G) [[], [6, 4], [4], [6, 5], [1, 2, 7], [3], [1, 3], [4]]

dfs(1)

for i in range(2, N+1) :
    print(tree[i])
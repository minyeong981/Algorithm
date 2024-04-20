def dfs(s):
    st = []
    st.append(s)
    visited = [False] * (N + 1)
    visited[s] = True
    cnt = 0

    while st:
        v = st.pop()
        for w in G[v]:
            if not visited[w]:
                st.append(w)
                visited[w] = True
                cnt += 1

    return cnt

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    G = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    #print(G) [[], [2, 3], [1, 3], [2, 1]]

    Cnt = dfs(1)
    print(Cnt)
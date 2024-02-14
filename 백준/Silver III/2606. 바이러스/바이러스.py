def virus(s):
    cnt = 0
    st = []
    visited = [False]*(N+1)
    st.append(s)
    visited[s] = True
    while st:
        v = st.pop()
        cnt += 1
        for w in G[v] :
            if not visited[w] :
                st.append(w)
                visited[w] = True

    return cnt-1



N = int(input())
E = int(input())

G = [[]*(N+1) for _ in range(N+1)]
for i in range(E):
    v1, v2 = map(int, input().split())
    G[v1].append(v2)
    G[v2].append(v1)

result = virus(1)
print(result)
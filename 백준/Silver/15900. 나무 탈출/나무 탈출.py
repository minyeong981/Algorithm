import sys
input = sys.stdin.readline

def dfs(root) :
    st = [root]
    visited[root] = True
    while st:
        v = st.pop()
        for w in G[v]:
            if not visited[w]:
                visited[w] = True
                st.append(w)
                node[w] = node[v] + 1


n = int(input())

G = [[] for _ in range(n+1)]
visited = [False]*(n+1)
node = [0]*(n+1)

# 양 방향 그래프 만들기
for _ in range(n-1) :
    v1, v2 = list(map(int, input().split()))
    G[v1].append(v2)
    G[v2].append(v1)
# print(G)

dfs(1)

result = 0
# 루트노드에서 리프노드까지의 거리 세기
for i in range(2, n+1):
    if len(G[i]) == 1 : # 리프노드면
        result += node[i]

if result%2 == 0 : # 성원이가 먼저 시작하니까
    print('No')
else :
    print('Yes')
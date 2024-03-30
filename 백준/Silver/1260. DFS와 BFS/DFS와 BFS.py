from collections import deque
def bfs(s) :
    q = deque()
    q.append(s)
    visited = [False] * (N+1)
    visited[s] = True
    while q :
        v = q.popleft()
        print(v, end=' ')

        for w in G[v] :
            if not visited[w] :
                q.append(w)
                visited[w] = True

def dfs(s) :
    visited[s] = True
    print(s, end=' ')
    for w in G[s] :
        if not visited[w] :
            dfs(w)


N, M, V = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    v1, v2 = map(int, input().split())
    G[v1].append(v2)  #양방향
    G[v2].append(v1)
# print(G) #[[], [2, 3], [5, 1], [4, 1], [5, 3], [4, 2]]

for i in range(N+1): #정점이 두 개 이상일 때 작은 거부터 가도록 정렬해놓기
    G[i].sort()
# print(G) #[[], [2, 3], [1, 5], [1, 4], [3, 5], [2, 4]]

visited = [False] * (N+1) #dfs는 재귀로 풀기
dfs(V)

print()
bfs(V)
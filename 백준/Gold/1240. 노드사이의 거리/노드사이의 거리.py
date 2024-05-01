import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(s,e, totalDist):
    visited[s] = True

    if s == e :
        return totalDist

    for w, dist in tree[s] :
        if not visited[w] :
            result = dfs(w, e, totalDist+dist)
            if result is not None:
                return result


n, m = map(int, input().split())

# 트리 만들 때 양방향, 거리 같이 넣기
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    v1, v2, dist = list(map(int, input().split()))
    tree[v1].append((v2, dist))
    tree[v2].append((v1, dist))
# print(tree) [[], [(2, 2), (4, 3)], [(1, 2)], [(4, 2)], [(3, 2), (1, 3)]]


for _ in range(m):
    visited = [False] * (n+1)
    s, e = map(int, input().split())
    print(dfs(s,e,0)) # 시작점, 끝점, 거리
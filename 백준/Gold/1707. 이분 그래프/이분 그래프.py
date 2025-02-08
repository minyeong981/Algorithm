import sys
from collections import deque
input = sys.stdin.readline

def is_bipartite(V, E):
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    color = [0] * (V + 1)

    def bfs(start):
        queue = deque([start])
        color[start] = 1

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if color[neighbor] == 0:  # 방문하지 않은 경우
                    color[neighbor] = -color[node]  # 현재 노드와 반대 색상으로 칠함
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:  # 같은 색상이면 이분 그래프 아님
                    return False
        return True

    for i in range(1, V + 1):
        if color[i] == 0:  # 방문하지 않은 노드에 대해 BFS 수행
            if not bfs(i):
                return "NO"

    return "YES"

K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    print(is_bipartite(V, E))

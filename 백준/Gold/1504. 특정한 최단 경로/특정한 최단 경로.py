import heapq
import sys
input = sys.stdin.readline

def solve(s, target):
    heap = []
    visited = [float('inf')] * (N + 1)
    heapq.heappush(heap, (0, s))
    visited[s] = 0
    
    while heap:
        w, curr = heapq.heappop(heap)

        if visited[curr] < w:
            continue

        for next, nextW in g[curr]:
            newW = nextW + w
            if visited[next] > newW:
                visited[next] = newW
                heapq.heappush(heap, (newW, next))

    return visited[target] if visited[target] != float('inf') else -1

N, E = map(int, input().split())
g = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))

v1, v2 = map(int, input().split())

# 다익스트라 실행
sTov1 = solve(1, v1)
sTov2 = solve(1, v2)
v1Tov2 = solve(v1, v2)
v1ToE = solve(v1, N)
v2ToE = solve(v2, N)

# 한 경로라도 갈 수 없는 경우 확인
if -1 in [sTov1, sTov2, v1Tov2, v1ToE, v2ToE]:
    print(-1)
else:
    result = min(sTov1 + v1Tov2 + v2ToE, sTov2 + v1Tov2 + v1ToE)
    print(result)

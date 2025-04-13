import heapq
import sys
input = sys.stdin.readline

def solve(X) :
    q = []
    heapq.heappush(q, (0, X))
    visited = [float('inf')] * (N + 1)
    visited[X] = 0
    while q :
        dist, city = heapq.heappop(q)

        if visited[city] < dist :
            continue

        for nextDist, nextC in path[city] :
            newDist = dist + nextDist
            if visited[nextC] > newDist :
                visited[nextC] = newDist
                heapq.heappush(q, (newDist, nextC))
                
    return visited

N, M, K, X = map(int, input().split())
path = [[] for _ in range(N + 1)]
for _ in range(M) :
    A, B = map(int, input().split())
    path[A].append((1, B))
arr = solve(X)

result = []
for i in range(1, N + 1) :
    if arr[i] == K :
        result.append(i)
        
print('\n'.join(map(str, sorted(result))) if len(result) != 0 else -1)
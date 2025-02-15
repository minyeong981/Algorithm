import heapq
import sys
input = sys.stdin.readline

def dij(s, target) :
    q = []
    visited = [float('inf')] * (N + 1)
    heapq.heappush(q, (0, s))
    visited[s] = 0
    while q :
        cost, start = heapq.heappop(q)

        if start == target :
            return cost

        if visited[start] < cost :
            continue

        for eC, bus in G[start] :
            value = bus + cost
            if visited[eC] > value :
                visited[eC] = value
                heapq.heappush(q, (value, eC))

N = int(input())
M = int(input())
G = [[] for _ in range(N + 1)]
for _ in range(M) :
    sC, eC, bus = map(int, input().split())
    G[sC].append((eC, bus))
sTarget, eTarget = map(int, input().split())
print(dij(sTarget, eTarget))
import heapq
import sys
input = sys.stdin.readline

def dij() :
    q = []
    heapq.heappush(q, (0, K)) # 가중치, 시작점
    visited = [INF] * (V + 1)
    visited[K] = 0
    while q :
        currWeight, currNode = heapq.heappop(q)

        if visited[currNode] < currWeight :
            continue

        for nextNode, nextWeight in G[currNode] :
            dist = currWeight + nextWeight
            if visited[nextNode] > dist :
                visited[nextNode] = dist
                heapq.heappush(q, (dist, nextNode))

    for i in range(1, V + 1):
        if visited[i] == INF:
            print('INF')
        else:
            print(visited[i])



V, E = map(int, input().split())
K = int(input())
G = [[] for _ in range(V + 1)]
INF = float('inf')
for _ in range(E) :
    u, v, w = map(int, input().split())
    G[u].append((v, w))
dij()

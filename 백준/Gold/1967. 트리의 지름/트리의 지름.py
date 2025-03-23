import heapq
import sys
input = sys.stdin.readline

def findFarestNode(s, w) :
    heap = [(0, s)]
    visited = [float('inf')] * (n + 1)
    visited[s] = 0
    while heap :
        currW, node = heapq.heappop(heap)

        if visited[node] < currW :
            continue

        for next, nextW in tree[node] :
            newW = currW + nextW
            if visited[next] > newW :
                visited[next] = newW
                heapq.heappush(heap, (newW, next))

        if len(heap) == 0 :
            return node, currW

n = int(input().strip())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1) :
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

# 임의의 노드 1에서 가장 먼 노드 찾기
farestNode, _ = findFarestNode(1, 0)
_, result = findFarestNode(farestNode, 0)
print(result)
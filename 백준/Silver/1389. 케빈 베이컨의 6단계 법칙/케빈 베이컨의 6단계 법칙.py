import heapq
import sys
input = sys.stdin.readline

def solve(p) :
    cnt = 0
    visited = [float('inf')] * (N + 1)
    fDic = {}
    for i in range(1, N + 1) :
        fDic[i] = 0
    pq = []
    heapq.heappush(pq, (0, p))
    while pq :
        w, me = heapq.heappop(pq)

        if me != p and fDic[me] == 0 :
            fDic[me] = w

        for friend in g[me] :
            if visited[friend] > w :
                visited[friend] = w
                heapq.heappush(pq, (w + 1, friend))

    for _, v in fDic.items() :
        cnt += v

    return cnt, p

N, M = map(int, input().split())
g = [[] for _ in range(N + 1)]
for i in range(1, M + 1) :
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

heap = []
for j in range(1, N + 1) :
    heapq.heappush(heap, (solve(j)))
level, result = heapq.heappop(heap)
print(result)
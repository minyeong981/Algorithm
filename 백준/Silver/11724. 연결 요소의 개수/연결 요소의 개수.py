from collections import deque
import sys
input = sys.stdin.readline

def count() :
    cnt = 0
    visited = [False] * (N + 1)
    for i in range(1, N + 1) :
        q = deque([i])
        if visited[i] :
            continue

        while q :
            x = q.popleft()

            for y in G[x] :
                if not visited[y] :
                    visited[y] = True
                    q.append(y)
        cnt += 1
    return cnt

N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]

for _ in range(M) :
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

print(count())
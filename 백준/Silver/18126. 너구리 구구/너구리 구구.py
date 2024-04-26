import sys
input = sys.stdin.readline
from collections import deque

def bfs(s):
    global maxDist
    q = deque()
    q.append((s,0))
    visited = [False]*(n+1)
    visited[1] = True

    while q :
        now, dist = q.popleft()

        for next, roomDist in room[now] :
            if not visited[next] :
                q.append((next, dist+roomDist))
                visited[next] = True
                maxDist = max(maxDist, dist+roomDist)

n = int(input())

room = [[] for _ in range(n+1)]
for _ in range(n-1):
    A, B, C = map(int, input().split())
    room[A].append((B, C))
    room[B].append((A, C))
    
# print(room) #[[], [(2, 3)], [(1, 3), (3, 2), (4, 4)], [(2, 2)], [(2, 4)]]
maxDist = 0
bfs(1)
print(maxDist)
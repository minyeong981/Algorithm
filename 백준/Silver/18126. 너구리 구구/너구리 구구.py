from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)


def dfs(s, visitedRoom, distance):
    global maxDist

    for relatedRoom, dist in room[s]:
        if relatedRoom != visitedRoom:
            dfs(relatedRoom, s, distance + dist)

    maxDist = max(maxDist, distance)


n = int(input())

room = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    A, B, C = map(int, input().split())
    room[A].append((B, C))
    room[B].append((A, C))

maxDist = 0
dfs(1, 0, 0)
print(maxDist)
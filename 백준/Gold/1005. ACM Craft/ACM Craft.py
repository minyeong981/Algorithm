from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t) :
    n, k = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    indegree = [0] * (n+1) # 선행 건물 수
    dp = [0] * (n+1)       # 각 건물까지의 최소 시간

    for _ in range(k) :
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1

    w = int(input())

    queue = deque()
    for i in range(1, n+1) :
        if indegree[i] == 0 :
            queue.append(i)
            dp[i] = time[i]

    while queue :
        current = queue.popleft()

        for next_building in graph[current] :
            indegree[next_building] -= 1
            dp[next_building] = max(dp[next_building], dp[current] + time[next_building])
            if indegree[next_building] == 0 :
                queue.append(next_building)
    print(dp[w])
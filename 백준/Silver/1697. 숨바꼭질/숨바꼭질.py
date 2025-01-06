from collections import deque

def findFastTime(N, K) :
    visited = [False] * 100001
    queue = deque([(N, 0)]) # 현재 위치, 시간

    while queue :
        position, time = queue.popleft()

        if position == K :
            return time

        for next in (position+1, position-1, 2*position) :
            if 0 <= next <= 100000 and not visited[next] :
                visited[next] = True
                queue.append((next, time+1))


import sys
input = sys.stdin.readline()

N, K = map(int, input.split())

print(findFastTime(N, K))
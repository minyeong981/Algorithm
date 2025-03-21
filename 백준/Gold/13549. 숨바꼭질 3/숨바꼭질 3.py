import heapq
import sys
input = sys.stdin.readline

def solve(s, target) :
    path = []
    heapq.heappush(path, (0, s))
    time = [float('inf')] * 100001
    time[s] = 0
    while path :
        currTime, currPos = heapq.heappop(path)

        if currPos == target :
            return currTime

        for nextPos in [currPos + 1, currPos - 1, 2 * currPos] :
            if 0 <= nextPos <= 100000 :
                if abs(currPos - nextPos) == 1 and time[nextPos] > currTime + 1:
                    time[nextPos] = currTime + 1
                    heapq.heappush(path, (time[nextPos], nextPos))
                elif nextPos == 2 * currPos and time[nextPos] > currTime:
                    time[nextPos] = currTime
                    heapq.heappush(path, (time[nextPos], nextPos))

N, K = map(int, input().split())
print(solve(N, K))
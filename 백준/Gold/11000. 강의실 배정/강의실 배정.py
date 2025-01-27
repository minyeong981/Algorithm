import heapq
import sys
input = sys.stdin.readline

n = int(input())

classLst = []
current = []
for i in range(n) :
    s, e = map(int, input().split())
    classLst.append([s, e])

classLst.sort()
heapq.heappush(current, classLst[0][1])

for i in range(1, n) :
    if classLst[i][0] < current[0] :
        heapq.heappush(current, classLst[i][1])
    else :
        heapq.heappop(current)
        heapq.heappush(current, classLst[i][1])

print(len(current))
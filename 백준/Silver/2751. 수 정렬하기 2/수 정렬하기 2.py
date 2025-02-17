import heapq
import sys
input = sys.stdin.readline

heap = []
N = int(input().strip())
for _ in range(N) :
    heapq.heappush(heap, int(input().strip()))

i = 0
while i < N :
    print(heapq.heappop(heap))
    i += 1
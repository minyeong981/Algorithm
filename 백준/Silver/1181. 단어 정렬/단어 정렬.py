import heapq
import sys
input = sys.stdin.readline

N = int(input().rstrip())
string = set()
for _ in range(N) :
    string.add(input().rstrip())

heap = []
for ele in string :
    heapq.heappush(heap, (len(ele), ele))

for _ in range(len(string)) :
    _, result = heapq.heappop(heap)
    print(result)
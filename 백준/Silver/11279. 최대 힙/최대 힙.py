import heapq
from sys import stdin

n = int(stdin.readline())
lst = []

for _ in range(n) :
    x = int(stdin.readline())

    if x == 0 :
        if lst :
            print(heapq.heappop(lst)[1])
        else :
            print(0)
    else:
        heapq.heappush(lst, [-x,x])

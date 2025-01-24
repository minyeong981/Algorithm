import heapq
import sys
input = sys.stdin.readline

N = int(input())
lst = []

for _ in range(N) :
    x = int(input())

    if x == 0 :
        if len(lst) == 0 :
            print(0)
        else :
            absV, origV = heapq.heappop(lst) # 1. 절댓값 기준 최솟값, 같다면? 2. 원래 값 기준 최솟값
            print(origV)
    else :
        heapq.heappush(lst, (abs(x), x)) # lst에 (절댓값 x, x) 넣기
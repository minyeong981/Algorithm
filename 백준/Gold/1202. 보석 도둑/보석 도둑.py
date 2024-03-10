from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
M_Vlst = []
for _ in range(N):
    M, V = map(int, input().split())
    M_Vlst.append((M, V))
M_Vlst.sort()  # 보석의 무게를 오름차순으로 정렬

bags = []
for _ in range(K):
    bags.append(int(input()))
bags.sort()  # 가방의 크기를 오름차순으로 정렬

i = 0
result = 0
price = [] # 가격 담을 리스트

for bag in bags:
    while i < len(M_Vlst) and M_Vlst[i][0] <= bag:  # 현재 가방에 넣을 수 있는 보석 후보군 추출
        heappush(price, -M_Vlst[i][1])
        i += 1
    if price :
        result += -heappop(price)
print(result)

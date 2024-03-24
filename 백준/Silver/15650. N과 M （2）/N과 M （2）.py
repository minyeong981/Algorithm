from itertools import combinations

N, M = map(int, input().split())
lst = []
for i in range(1, N+1):
    lst.append(i)
for combo in combinations(lst, M):
    print(*combo)
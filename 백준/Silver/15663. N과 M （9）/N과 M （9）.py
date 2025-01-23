from itertools import permutations

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
# lst.sort()

result = set(permutations(lst, M))
for ele in sorted(result) :
    print(*ele)
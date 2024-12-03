from collections import defaultdict
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lamps = [defaultdict(int) for _ in range(m+1)]
for _ in range(n) :
    s = input().strip()
    lamps[s.count('0')][s] += 1

k = int(input())
result = 0
for i in range(k%2, min(m+1, k+1), 2):
    for j in lamps[i].values() :
        result = max(result, j)
print(result)
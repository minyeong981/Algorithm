from bisect import bisect_left
import sys
input = sys.stdin.readline

N = int(input().strip())
lst = list(map(int, input().split()))
Xj = sorted(list(set(lst)))

for Xi in lst :
    print(bisect_left(Xj, Xi), end=' ')
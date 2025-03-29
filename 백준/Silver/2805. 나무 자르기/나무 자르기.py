import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tree = list(map(int, input().split()))
tree.sort()
s, e = 1, tree[-1]
maxh = 0
while s <= e :
    mid = (s + e) // 2
    cut = 0
    for meter in tree :
        if meter > mid :
            cut += meter - mid
    if cut >= M :
        if maxh < mid :
            maxh = mid
        s = mid + 1
    elif cut < M :
        e = mid - 1
print(maxh)
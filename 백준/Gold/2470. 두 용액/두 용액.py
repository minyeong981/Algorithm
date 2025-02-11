import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
lst.sort()

s, e = 0, N - 1
minV = float('inf')
result = []
while s < e :
    if minV > abs(lst[s] + lst[e]) :
        minV = abs(lst[s] + lst[e])
        result.append((lst[s], lst[e]))

    if lst[s] + lst[e] < 0 :
        s += 1
    else :
        e -= 1
print(*result.pop())
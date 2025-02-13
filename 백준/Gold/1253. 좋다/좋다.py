import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
lst.sort(reverse=True)

isGood = False
good = 0

for i in range(N) :
    s, e = 0, N - 1
    while s < e :
        if s == i :
            s += 1
            continue
        elif e == i :
            e -= 1
            continue

        if lst[s] + lst[e] == lst[i] :
            isGood = True
            good += 1
            break
        elif lst[s] + lst[e] > lst[i] :
            s += 1
        else :
            e -= 1
print(good)
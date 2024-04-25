def solve(lst):
    maxlst = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if lst[i] > lst[j] and maxlst[i] < maxlst[j] + 1:
                maxlst[i] = maxlst[j] + 1

    return max(maxlst)


n = int(input())
lst = list(map(int, input().split()))

print(solve(lst))

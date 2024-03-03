def findmaxV(num):
    lst = []
    lst.append(N)
    lst.append(num)

    i = 2
    while lst[i-2] - lst[i-1] >= 0 :
        lst.append(lst[i-2]-lst[i-1])
        i += 1
    return lst


N = int(input())
maxV = 0
for idx in range(N//2, N+1):
    if len(findmaxV(idx)) > maxV :
        maxV = len(findmaxV(idx))
        lst = findmaxV(idx)
print(maxV)
print(*lst)
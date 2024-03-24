def perm(k,lst):
    if len(lst) == M :
        print(*lst)
        return

    for i in range(1, N+1):
        if i not in lst :
            lst.append(i)
            perm(k+1, lst)
            lst.pop()

N, M = map(int, input().split())
perm(1,[])
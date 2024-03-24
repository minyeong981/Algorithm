def perm(lst):
    if len(lst) == M:
        print(*lst)
        return

    for i in range(1,N+1):
        lst.append(i)
        perm(lst)
        lst.pop()


N, M = map(int, input().split())
perm([])
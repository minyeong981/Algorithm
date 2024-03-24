def perm(lst):
    if len(lst) == M :
        print(*lst)
        return

    for i in A :
        lst.append(i)
        perm(lst)
        lst.pop()

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
perm([])
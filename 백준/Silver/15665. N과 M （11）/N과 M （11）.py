def perm(k):
    if len(path) == M :
        lst.add(tuple(path.copy()))
        return
    if k == N :
        return

    for i in range(N):
        path.append(A[i])
        perm(k+1)
        path.pop()

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
path = []
lst = set()
perm(0)
for i in sorted(lst) :
    print(*i)
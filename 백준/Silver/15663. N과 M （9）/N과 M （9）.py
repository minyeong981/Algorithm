def perm(k, lst):
    if len(lst) == M :
        result.add(tuple(lst.copy()))
        return

    for i in range(N):
        if not visited[i]:
            lst.append(A[i])
            visited[i] = True
            perm(k+1, lst)
            lst.pop()
            visited[i] = False

N, M = map(int, input().split())
A = list(map(int, input().split()))
visited = [False for _ in range(N)]
result = set()
perm(0, [])

for ans in sorted(result) :
    print(' '.join(map(str, ans)))

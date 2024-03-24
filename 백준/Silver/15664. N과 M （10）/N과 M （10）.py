def combi(k, lst):
    if len(lst) == M :
        result.add(tuple(lst.copy()))
        return

    for i in range(k, N):
        lst.append(A[i])
        combi(i+1, lst)
        lst.pop()


N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
result = set()
combi(0,[])

for i in sorted(result) :
    print(' '.join(map(str, i)))
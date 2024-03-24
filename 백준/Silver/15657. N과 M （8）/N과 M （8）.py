def combi(k,lst):
    if len(lst) == M :
        print(*lst)
        return

    for i in range(k, N):
        lst.append(A[i])
        combi(i, lst)
        lst.pop()

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
combi(0,[])
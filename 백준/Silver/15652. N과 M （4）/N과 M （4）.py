def combi(k,s):
    if len(s) == M :
        print(' '.join(s))
        return

    for i in range(k, N+1):
        combi(i, s+str(i))

N, M = map(int, input().split())
combi(1,'')
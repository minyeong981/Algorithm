N, K = map(int, input().split())
newlst = []
for num in range(1,N+1) :
    if N%num == 0 :
        newlst.append(num)

if len(newlst) < K :
    print(0)
else :
    print(newlst[K-1])
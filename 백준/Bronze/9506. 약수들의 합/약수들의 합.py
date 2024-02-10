while True :
    N = int(input())
    if N == -1 :
        break
    newlst = []
    for num in range(1, N+1) :
        if N%num == 0 :
            newlst.append(num)
    newlst.pop()
    sumV =0
    for ele in newlst :
        sumV += ele
    if sumV == N :
        print(f'{N} =',' + '.join(map(str, newlst)))
    else :
        print(f'{N} is NOT perfect.')
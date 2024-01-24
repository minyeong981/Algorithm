N = int(input())

def facto(N) :
    if N ==0:
        return 1
    
    return N*facto(N-1)
print(facto(N))
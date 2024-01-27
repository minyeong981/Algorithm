N, M = map(int, input().split())
lst = [0]*N

for cnt in range(M) :
    i, j, k = map(int, input().split())
    for idx in range(i, j+1) :
        lst[idx-1] = k

print(*lst, end = '')
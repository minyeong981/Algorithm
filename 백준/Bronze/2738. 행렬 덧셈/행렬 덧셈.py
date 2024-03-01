N, M = map(int, input().split())
arrA = [list(map(int,input().split())) for _ in range(N)]
arrB = [list(map(int,input().split())) for _ in range(N,N+N)]
#print(arrA,arrB)
result = []

for row in range(N):
    for col in range(M) :
        result.append(arrA[row][col] + arrB[row][col])

for i in range(0, len(result),M):
    print(*result[i:M+i], end=' ')
    print()

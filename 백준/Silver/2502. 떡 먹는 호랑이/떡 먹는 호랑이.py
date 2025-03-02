import sys
input = sys.stdin.readline

def solve(d, dCnt, x, y) :
    global K
    while dCnt <= d and x+y <= K :
        if dCnt == d :
            if K == x+y:
                return x, y
        dCnt += 1
        preX = x
        x = y
        y = preX+y
    return 0, 0

D, K = map(int, input().split())

for i in range(1, K + 1) :
    for j in range(i, K + 1) :
        A, B = solve(D, 3, i, j)
        if (A, B) != (0, 0) :
            print(i)
            print(j)
            exit()

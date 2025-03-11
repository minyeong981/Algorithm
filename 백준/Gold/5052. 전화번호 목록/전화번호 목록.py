import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t) :
    n = int(input().strip())
    lst = sorted([input().strip() for _ in range(n)])
    for i in range(n - 1) :
        if lst[i] == lst[i+1][:len(lst[i])] :
            print('NO')
            break
    else :
        print('YES')
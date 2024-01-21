i = 0
while True :
    i += 1
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0 :
        break
    a = V//P
    b = V%P
    if L < b :
        b = L
    print(f'Case {i}: {a*L+b}')

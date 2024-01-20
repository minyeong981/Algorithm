H, M = map(int, input().split())

if M >= 45 :
    minute = M - 45
    print(H, minute)
else :
    hour = H - 1
    if H == 0 :
        hour = 23
    minute = M + 15
    print(hour, minute)

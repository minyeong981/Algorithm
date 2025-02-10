import sys
input = sys.stdin.readline

A, B = map(int, input().split())
cnt = 0
while A != B :
    if B > A and B % 2 == 0 :
        B //= 2
        cnt += 1
    elif B > A and str(B)[-1] == '1' :
        B = int(str(B)[:len(str(B))-1])
        cnt += 1
    else :
        cnt = -2
        break

print(cnt + 1)
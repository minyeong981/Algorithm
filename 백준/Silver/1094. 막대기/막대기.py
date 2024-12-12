import sys
input = sys.stdin.readline

x = int(input())
stick = [64]
cnt = 1

while sum(stick) != x :
    if sum(stick) > x :
        stick.sort()
        stick[0] //= 2
        if sum(stick) < x :
            stick.append(stick[0])
            cnt += 1

print(cnt)
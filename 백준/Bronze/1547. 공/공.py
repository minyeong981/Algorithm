import sys
input = sys.stdin.readline

m = int(input().strip())
cups = [i for i in range(4)]
for _ in range(m) :
    x, y = map(int, input().split())
    xi = cups.index(x)
    yi = cups.index(y)
    cups[xi], cups[yi] = cups[yi], cups[xi]

print(cups[1])
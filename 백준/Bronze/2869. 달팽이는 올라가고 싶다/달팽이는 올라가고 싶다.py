import sys
input = sys.stdin.readline

A, B, V = map(int, input().split())
cnt = (V-B)/(A-B)
print(int(cnt) if cnt == int(cnt) else int(cnt)+1)
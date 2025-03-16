import sys
input = sys.stdin.readline

N = int(input().strip())
members = []
for _ in range(N) :
    member = list(input().split())
    members.append([int(member[0]), member[1]])
result = sorted(members, key=lambda x:x[0])
for v in result :
    print(*v)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dicS = {}
for _ in range(N) :
    dicS[input()] = 0

for _ in range(M) :
    string = input()
    if dicS.get(string, -1) != -1 :
        dicS[string] += 1

print(sum(dicS.values()))
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solve(t) :
    global cnt
    for w in workLst[t] :
        if not visited[w] :
            visited[w] = True
            cnt += 1
            solve(w)


N, M = map(int, input().split())
workLst = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
cnt = 0
for _ in range(M) :
    a, b = map(int, input().split())
    workLst[b].append(a)
target = int(input().strip())
solve(target)
print(cnt)
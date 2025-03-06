import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(s) :
    stack = [s]
    visited = [False] * (n + 1)
    visited[s] = True
    cnt = 0
    while stack :
        v = stack.pop()

        for w in g[v] :
            if not visited[w] :
                visited[w] = True
                stack.append(w)
                cnt += 1

        if len(stack) == 0 and all(visited[1:]) and cnt == e :
            return 'tree'

    return 'graph'

t = int(input().strip())
for _ in range(t) :
    n = int(input().strip())
    e = int(input().strip())
    g = [[] for _ in range(n + 1)]
    for _ in range(e) :
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)
    print(dfs(1))
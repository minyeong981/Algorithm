import sys
input = sys.stdin.readline

def solve(N, lst) :
    g = [[] for _ in range(N + 1)]

    i = 1
    for j in lst :
        g[i] = [j]
        i += 1
    return g

def countCycle() :
    visited = [False]*(N + 1)
    cnt = 0

    for i in range(1, N+1) :
        stack = [i]

        if visited[i] == False :
            while stack  :
                x = stack.pop()

                for v in graph[x] :
                    if not visited[v] :
                        visited[v] = True
                        stack.append(v)
            cnt += 1
    return cnt

T = int(input())
for _ in range(T) :
    N = int(input())
    lst = list(map(int, input().split()))
    graph = solve(N, lst)
    print(countCycle())
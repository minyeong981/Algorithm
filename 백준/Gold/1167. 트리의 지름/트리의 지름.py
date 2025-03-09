import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node, weight) :
    global farthestN, maxV

    if weight > maxV :
        maxV = weight
        farthestN = node

    for otherN, otherW in tree[node] :
        if not visited[otherN] :
            visited[otherN] = True
            dfs(otherN, weight + otherW)

V = int(input().strip())
tree = [[] for _ in range(V + 1)]
for _ in range(V) :
    lst = list(map(int, input().split()))
    end = 1
    while lst[end] != -1 :
        tree[lst[0]].append((lst[end], lst[end + 1]))
        end += 2


visited = [False] * (V + 1)
visited[1] = True
maxV = 0
farthestN = 0
dfs(1, 0)

visited = [False] * (V + 1)
visited[farthestN] = True
maxV = 0
dfs(farthestN, 0)

print(maxV)
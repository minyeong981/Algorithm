def dfs(start):
    global cnt
    visited[start] = True
    leaf = True
    for w in tree[start]:
        if not visited[w]:
            leaf = False
            dfs(w)
    if leaf:
        cnt += 1

n = int(input())
nodeList = list(map(int, input().split()))
removeNode = int(input())

cnt = 0

#트리 만들기
tree = [[] for _ in range(n)]
root = -1
for i in range(n):
    if nodeList[i] == -1:
        root = i
    else:
        tree[nodeList[i]].append(i)

visited = [False] * n

if removeNode != root:
    visited[removeNode] = True
    dfs(root)
else:
    cnt = 0

print(cnt)


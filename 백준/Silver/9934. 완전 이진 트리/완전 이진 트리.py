def dfs(inorder, depth):
    mid = (len(inorder)//2)
    Tree[depth].append(inorder[mid])
    if len(inorder) == 1 :
        return
    dfs(inorder[:mid], depth+1)
    dfs(inorder[mid+1:], depth+1)

K = int(input())
Bnum = list(map(int, input().split()))
Tree = [[] for _ in range(K)]
dfs(Bnum, 0)

for i in Tree :
    print(*i)

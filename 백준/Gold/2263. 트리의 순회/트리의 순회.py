import sys
sys.setrecursionlimit(10**9)

def preorder(inorder_s, inorder_e, postorder_s, postorder_e) :
    if inorder_s > inorder_e or postorder_s > postorder_e :
        return
    root = postorder_lst[postorder_e]
    print(root, end = ' ')
    
    left = TREE[root] - inorder_s
    right = inorder_e - TREE[root]
    
    preorder(inorder_s, TREE[root]-1, postorder_s, postorder_s+left-1)
    preorder(TREE[root]+1, inorder_e, postorder_e-right, postorder_e-1)

n = int(input())

inorder_lst = list(map(int, input().split()))
postorder_lst = list(map(int, input().split()))

TREE = [0]*(n+1)
for i in range(n):
    TREE[inorder_lst[i]] = i

preorder(0, n-1, 0, n-1)
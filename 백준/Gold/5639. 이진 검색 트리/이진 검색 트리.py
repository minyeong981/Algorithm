import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.read  # read()를 사용하여 전체 입력을 빠르게 처리

# 입력 처리
values = list(map(int, input().split()))  # 입력을 한 번에 받아 리스트로 변환

# BST 구성 (스택을 이용한 반복 삽입)
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_bst(values):
    root = Node(values[0])  # 첫 번째 값이 루트
    for value in values[1:]:
        node = root
        while True:  # 적절한 위치를 찾을 때까지 반복
            if value < node.value:
                if node.left is None:
                    node.left = Node(value)
                    break
                else:
                    node = node.left
            else:
                if node.right is None:
                    node.right = Node(value)
                    break
                else:
                    node = node.right
    return root

# 후위 순회 (재귀)
def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.value)

# 트리 구축
root = build_bst(values)

# 후위 순회 실행
postorder(root)

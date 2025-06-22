import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)
    if rootX != rootY:
        parent[rootY] = rootX

n = int(input())
m = int(input())
parent = [i for i in range(n + 1)]

# 연결 정보로 유니온 수행
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    for j in range(1, n + 1):
        if data[j - 1] == 1:
            union(parent, i, j)

plan = list(map(int, input().split()))
root = find(parent, plan[0])

# 모든 도시가 같은 root를 가지는지 확인
for city in plan:
    if find(parent, city) != root:
        print("NO")
        break
else:
    print("YES")

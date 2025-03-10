import sys

# 빠른 입력
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 유니온 파인드: 루트 노드 찾기 (경로 압축)
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # 경로 압축 최적화
    return parent[x]

# 유니온 파인드: 두 집합 합치기
def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX < rootY:
        parent[rootY] = rootX
    else:
        parent[rootX] = rootY

# 입력 처리
n, m = map(int, input().split())
logs = []
parent = [i for i in range(n + 1)]

# 통나무 입력
for i in range(1, n + 1):
    s, e, _ = map(int, input().split())
    logs.append((s, e, i))  # (시작, 끝, 인덱스) 저장

# ✅ `x1` 기준 정렬 (좌표 순서대로 병합하기 위해 정렬)
logs.sort()

# ✅ 유니온 파인드로 같은 그룹 묶기
prev_x1, prev_x2, prev_idx = logs[0]

for i in range(1, n):
    x1, x2, idx = logs[i]

    # 겹치는 경우 병합
    if x1 <= prev_x2:
        union(prev_idx, idx)
        prev_x2 = max(prev_x2, x2)  # 끝점 업데이트
    else:
        prev_x1, prev_x2, prev_idx = x1, x2, idx  # 새로운 그룹 시작

# ✅ 질의 처리
result = []
for _ in range(m):
    a, b = map(int, input().split())
    result.append("1" if find(a) == find(b) else "0")

# ✅ 결과 출력 최적화
sys.stdout.write("\n".join(result) + "\n")
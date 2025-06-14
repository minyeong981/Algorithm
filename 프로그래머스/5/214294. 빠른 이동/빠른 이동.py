# 최적화된 전체 파이썬 코드 (시간 초과 방지 포함)

from collections import defaultdict

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
        self.rank[1] = float('inf')

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                if self.rank[rootX] == self.rank[rootY]:
                    self.rank[rootX] += 1

    def get_uniques(self):
        return [i for i in range(1, len(self.parent)) if self.parent[i] == i]

def solution(n, roads):
    uf = UnionFind(n + 1)
    toward_groups = [[] for _ in range(n + 1)]
    for a, b in roads:
        toward_groups[a].append(b)

    visited = [0] * (n + 1)
    stack_index = [None] * (n + 1)
    stack_index[1] = 0
    visited[1] = 1

    def dfs(cur, stack):
        for nxt in toward_groups[cur]:
            prefixed = uf.find(nxt)
            if not visited[prefixed]:
                visited[prefixed] = 1
                stack.append(prefixed)
                stack_index[prefixed] = len(stack) - 1
                dfs(prefixed, stack)
                stack.pop()
                stack_index[prefixed] = None
            else:
                idx = stack_index[prefixed]
                if idx is not None:
                    value = stack[idx]
                    root_value = uf.find(value)
                    uf.rank[root_value] = float('inf')
                    for i in range(idx + 1, len(stack)):
                        uf.union(value, stack[i])

    dfs(1, [1])

    prefix_toward_groups = [[] for _ in range(n + 1)]
    for a, b in roads:
        pa = uf.find(a)
        pb = uf.find(b)
        if pa != pb:
            prefix_toward_groups[pa].append(pb)

    toward_directly = [set() for _ in range(n + 1)]
    visited2 = [False] * (n + 1)

    def dfs2(x):
        if visited2[x]:
            return toward_directly[x]
        visited2[x] = True
        for nxt in prefix_toward_groups[x]:
            toward_directly[x].add(nxt)
            toward_directly[x].update(dfs2(nxt))
        return toward_directly[x]

    dfs2(1)

    uniques = uf.get_uniques()
    from_directly = [set() for _ in range(n + 1)]
    for u in uniques:
        for v in toward_directly[u]:
            from_directly[v].add(u)

    assigns = [0] * (n + 1)

    def b_matching(x, visited_set):
        for f in from_directly[x]:
            if f in visited_set:
                continue
            visited_set.add(f)
            if assigns[f] == 0 or b_matching(assigns[f], visited_set):
                assigns[f] = x
                return True
        return False

    result = 0
    for u in uniques:
        if b_matching(u, set()):
            result += 1

    return len(uniques) - result - 1


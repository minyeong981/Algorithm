from collections import deque
import sys
input = sys.stdin.readline

def solve(X, K) :
    q = deque([X])
    visited = [-1] * (N + 1)
    visited[X] = 0
    while q :
        city = q.popleft()

        if visited[city] > K : # 시간 단축 코드
            continue

        for nextC in path[city] :
            if visited[nextC] == -1 and visited[nextC] + 1 < K :
                visited[nextC] = visited[city] + 1
                q.append(nextC)

    return visited

N, M, K, X = map(int, input().split())
path = [[] for _ in range(N + 1)]
for _ in range(M) :
    A, B = map(int, input().split())
    path[A].append(B)
arr = solve(X, K)

result = []
for i in range(1, N + 1) :
    if arr[i] == K :
        result.append(i)
print('\n'.join(map(str, sorted(result))) if len(result) != 0 else -1)
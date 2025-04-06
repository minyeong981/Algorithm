from collections import deque
import sys
input = sys.stdin.readline

def solve(person, target) :
    q = deque()
    q.append(person)
    visited = [-1] * (n + 1)
    visited[person] = 0

    while q :
        p = q.popleft()

        if p == target :
            break

        for next in family[p] :
            if visited[next] == -1 :
                visited[next] = visited[p] + 1
                q.append(next)

    return visited[target]

n = int(input().strip())
who1, who2 = map(int, input().split())
m = int(input().strip())
family = [[] for _ in range(n + 1)]
for _ in range(m) :
    x, y = map(int, input().split())
    family[x].append(y)
    family[y].append(x)
print(solve(who1, who2))
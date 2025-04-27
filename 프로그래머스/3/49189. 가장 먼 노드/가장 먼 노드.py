from collections import deque, Counter
def bfs(start, n, g) :
    q = deque([start])
    visited = [0] * (n + 1)
    visited[start] = 1
    while q :
        x = q.popleft()
        
        for w in g[x] :
            if not visited[w] :
                visited[w] = visited[x] + 1
                q.append(w)
    
    maxV = max(visited)
    
    freList = Counter(visited)
    return freList[maxV]
    
                
def solution(n, edge):
    g = [[] for _ in range(n + 1)]
    for e in edge :
        g[e[0]].append(e[1])
        g[e[1]].append(e[0])
    
    return bfs(1, n, g)
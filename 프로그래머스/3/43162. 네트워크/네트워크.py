from collections import deque
def bfs(start, computers, visited, n) :
    q = deque([start])
    visited[start] = True
    while q :
        v = q.popleft()
        
        for i in range(n) :
            if computers[v][i] == 1 and not visited[i] :
                visited[i] = True
                q.append(i)

def solution(n, computers):
    visited = [False] * n
    answer = 0
    
    for i in range(n) :
        if not visited[i] :
            bfs(i, computers, visited, n)
            answer += 1
            
    return answer
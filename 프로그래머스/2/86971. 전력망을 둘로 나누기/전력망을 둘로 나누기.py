'''
(무조건) 트리 형태의 네트워크를 하나 끊었을 때 두 송전탑의 절댓값 차이가 최소가 되게 하라
'''
def dfs(start, tree, visited) :
    stack = [start]
    visited[start] = True
    cnt = 1
    while stack :
        node = stack.pop()
        for nextN in tree[node] :
            if not visited[nextN] :
                visited[nextN] = True
                stack.append(nextN)
                cnt += 1
    return cnt

def solution(n, wires):
    answer = n
    
    for i in range(len(wires)) :
        tree = [[] for _ in range(n+1)]
        
        # 간선 하나 제거
        for idx, (a, b) in enumerate(wires) :
            if i == idx :
                continue
            tree[a].append(b)
            tree[b].append(a)
        
        visited = [False] * (n+1)
        count = dfs(1, tree, visited)
        answer = min(answer, abs((n - count) - count))
    return answer
def solution(k, dungeons):
    n = len(dungeons)
    visited = [False] * n
    answer = 0
    
    def dfs(fatigue, count) :
        nonlocal answer
        answer = max(answer, count)
        
        for i in range(n) :
            min_fatigue, used_fatigue = dungeons[i]
            if not visited[i] and fatigue >= min_fatigue :
                visited[i] = True
                dfs(fatigue - used_fatigue, count + 1)
                visited[i] = False
        
    dfs(k, 0)
            
    return answer
def solution(begin, target, words):
    if target not in words:
        return 0

    n = len(words)
    answer = float('inf')
    visited = [False] * n

    # 한 글자만 다른지 확인하는 함수
    def is_convertible(word1, word2):
        count = 0
        for a, b in zip(word1, word2):
            if a != b:
                count += 1
        return count == 1

    def dfs(current, count):
        nonlocal answer
        if current == target:
            answer = min(answer, count)
            return
        
        for i in range(n):
            if not visited[i] and is_convertible(current, words[i]):
                visited[i] = True
                dfs(words[i], count + 1)
                visited[i] = False

    dfs(begin, 0)
    return answer if answer != float('inf') else 0

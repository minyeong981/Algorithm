def solution(info, n, m):
    visited = set()
    answer = float('inf')
    length = len(info)

    def dfs(index, a_total, b_total):
        nonlocal answer
        # 기저 조건
        if a_total >= n or b_total >= m:
            return
        if index == length:
            answer = min(answer, a_total)
            return

        # 현재 상태를 이미 방문했으면 종료
        state = (index, a_total, b_total)
        if state in visited:
            return
        visited.add(state)

        # A가 훔침
        dfs(index + 1, a_total + info[index][0], b_total)

        # B가 훔침
        dfs(index + 1, a_total, b_total + info[index][1])

    dfs(0, 0, 0)
    return answer if answer != float('inf') else -1

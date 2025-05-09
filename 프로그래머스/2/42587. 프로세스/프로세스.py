from collections import deque

def solution(priorities, location):
    queue = deque([(p, i) for i, p in enumerate(priorities)])
    answer = 0

    while queue:
        current = queue.popleft()
        if any(current[0] < q[0] for q in queue):  # 우선순위 높은 게 있으면 뒤로 보냄
            queue.append(current)
        else:
            answer += 1
            if current[1] == location:  # 우리가 찾는 인덱스면 종료
                return answer

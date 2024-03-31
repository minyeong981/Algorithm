from collections import deque

def bfs():
    q = deque()
    q.append((0, 0, 0))  # 시작점 (0, 0), 벽을 부순 적 없음
    visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]  # 벽을 부순 상태와 부수지 않은 상태의 방문 여부를 함께 관리

    while q:
        vr, vc, is_broken = q.popleft()

        if vr == N - 1 and vc == M - 1:  # 목적지에 도달한 경우
            return visited[vr][vc][is_broken] + 1  # 해당 위치까지의 최소 이동 횟수 반환

        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr = vr + dr
            nc = vc + dc

            if 0 <= nr < N and 0 <= nc < M:
                if MAP[nr][nc] == 1 and not is_broken:  # 벽을 만났는데 아직 벽을 부수지 않았다면
                    visited[nr][nc][1] = visited[vr][vc][0] + 1
                    q.append((nr, nc, 1)) # 벽을 한 번 부쉈으니까 그 다음부터는 벽(1)으로 갈 수 없음
                elif MAP[nr][nc] == 0 and not visited[nr][nc][is_broken]:  # 벽이 아니면서 방문하지 않았다면
                    visited[nr][nc][is_broken] = visited[vr][vc][is_broken] + 1
                    q.append((nr, nc, is_broken))

    return -1  # 목적지에 도달하지 못한 경우

N, M = map(int, input().split())
MAP = [list(map(int, input().rstrip())) for _ in range(N)]

result = bfs()
print(result)

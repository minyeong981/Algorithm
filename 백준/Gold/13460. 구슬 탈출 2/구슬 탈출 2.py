from collections import deque
import sys

input = sys.stdin.readline

def move(r, c, dr, dc):
    """벽을 만나거나 구멍에 빠질 때까지 이동"""
    cnt = 0  # 이동 거리
    while board[r + dr][c + dc] != '#' and board[r][c] != 'O':
        r += dr
        c += dc
        cnt += 1
    return r, c, cnt

def bfs():
    # 빨간 구슬과 파란 구슬 위치 큐에 삽입
    rq, bq = deque(), deque()
    
    # 초기 위치 찾기
    for r in range(N):
        for c in range(M):
            if board[r][c] == 'R':
                red_start = (r, c)
            elif board[r][c] == 'B':
                blue_start = (r, c)

    rq.append((*red_start, *blue_start, 0))  # (Rx, Ry, Bx, By, depth)
    visited = set()  # 방문 기록을 (Rx, Ry, Bx, By) 형태로 저장
    visited.add((*red_start, *blue_start))

    while rq:
        rx, ry, bx, by, depth = rq.popleft()

        if depth >= 10:  # 10번 이상 이동하면 실패
            return -1

        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nrx, nry, r_moves = move(rx, ry, dr, dc)
            nbx, nby, b_moves = move(bx, by, dr, dc)

            # 파란 구슬이 구멍에 빠지면 실패
            if board[nbx][nby] == 'O':
                continue

            # 빨간 구슬이 구멍에 빠지면 성공
            if board[nrx][nry] == 'O':
                return depth + 1

            # 두 구슬이 같은 위치에 있을 경우, 더 많이 이동한 구슬을 한 칸 뒤로 보냄
            if (nrx, nry) == (nbx, nby):
                if r_moves > b_moves:
                    nrx -= dr
                    nry -= dc
                else:
                    nbx -= dr
                    nby -= dc

            # 방문한 적 없는 상태라면 큐에 추가
            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))
                rq.append((nrx, nry, nbx, nby, depth + 1))

    return -1  # 10번 이내에 구멍에 도달하지 못하면 실패

# 입력 처리
N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

print(bfs())

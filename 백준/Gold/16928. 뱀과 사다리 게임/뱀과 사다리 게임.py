from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = list(range(101))

# 사다리 입력
for _ in range(N) :
    start, end = map(int, input().split())
    board[start] = end

# 뱀 입력
for _ in range(M) :
    snakeStart, snakeEnd = map(int, input().split())
    board[snakeStart] = snakeEnd

def playGame() :
    q = deque([(1, 0)]) # 현재 위치, 이동 횟수
    visited = [False]*101
    visited[1] = True

    while q :
        position, cnt = q.popleft()

        if position == 100 :
            return cnt

        for dice in range(1, 7) :
            next = position + dice
            if 0 < next < 101 and not visited[next] :
                visited[next] = True
                q.append((board[next], cnt + 1))

print(playGame())
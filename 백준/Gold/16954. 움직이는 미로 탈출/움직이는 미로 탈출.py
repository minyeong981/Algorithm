from collections import deque

def bfs(r,c) :
    q = deque()
    q.append((r,c))

    while q:
        
        for _ in range(len(q)):
            r, c = q.popleft()
            if maze[r][c] == '#':
                continue

            for dr, dc in [(-1,0),(0,-1),(0,1),(1,0),(1,-1),(-1,1),(-1,-1),(1,1),(0,0)] :
                nr, nc = r+dr, c+dc
                if 0 <= nr < 8 and 0 <= nc < 8 :
                    if maze[nr][nc] == '.' :
                        q.append((nr,nc))
                    if nr == 0 and nc == 7 :
                        return 1
                
        maze.pop() # 맨 아래 행 삭제
        maze.insert(0, ['.'] * 8) # 맨 위에 새로운 행 추가

maze = [list(input()) for _ in range(8)]

if bfs(7,0) == 1 :
    print(1)
else :
    print(0) # 욱제의 시작 위치

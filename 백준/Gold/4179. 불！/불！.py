from collections import deque

def bfs() :
    global cnt

    while jh :
        # 불 확산
        for _ in range(len(fire)):
            fx, fy = fire.popleft()
            for fdx, fdy in [(1,0),(0,1),(-1,0),(0,-1)]:
                fnx = fx + fdx
                fny = fy + fdy
                if 0 <= fnx < r and 0 <= fny < c and MAP[fnx][fny] == '.':
                    MAP[fnx][fny] = 'F'
                    fire.append((fnx, fny))

        # 지훈이 이동
        for _ in range(len(jh)) :
            jx, jy = jh.popleft()

            for jdx, jdy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                jnx = jx + jdx
                jny = jy + jdy
                if 0 <= jnx < r and 0 <= jny < c:
                    if MAP[jnx][jny] == '.':
                        MAP[jnx][jny] = 'J'
                        jh.append((jnx, jny))
                        if jnx == 0 or jnx == r - 1 or jny == 0 or jny == c - 1:
                            print(cnt+1)
                            return

        # 벽에 갇히는 경우 체크
        if not jh:
            print('IMPOSSIBLE')
            return

        cnt += 1

    print('IMPOSSIBLE')

r, c = map(int, input().split())
MAP = [list(input()) for _ in range(r)]

cnt = 1
jh = deque()
fire = deque()
finish = False

for i in range(r) :
    for j in range(c) :
        if MAP[i][j] == 'J' :
            jh.append((i,j))
            if i == 0 or i == r-1 or j == 0 or j == c-1 :
                finish = True
        elif MAP[i][j] == 'F' :
            fire.append((i,j))
if finish :
    print(cnt)
else :
    bfs()
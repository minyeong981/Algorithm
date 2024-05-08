def find(like, seats, n):
    maxCnt = -1
    maxEmpty = -1
    select = (-1, -1)

    for r in range(n):
        for c in range(n):
            if seats[r][c] == 0:  # 빈 자리인 경우에만 확인
                cnt = 0
                emptyCnt = 0
                for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < n and 0 <= nc < n:
                        if seats[nr][nc] in like: # 좋아하는 학생에 들어있으면
                            cnt += 1
                        elif seats[nr][nc] == 0:
                            emptyCnt += 1

                if cnt > maxCnt or (cnt == maxCnt and emptyCnt > maxEmpty):
                    maxCnt = cnt
                    maxEmpty = emptyCnt
                    select = (r, c) # 변경된 자리 위치

    return select

def calS(seats, like, n):
    satisfaction = 0 # 만족도

    for r in range(n):
        for c in range(n):
            cnt = 0
            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    if seats[nr][nc] in like[seats[r][c]]: # 좋아하는 학생 번호 있으면 cnt +1
                        cnt += 1

            if cnt == 1:
                satisfaction += 1
            elif cnt == 2:
                satisfaction += 10
            elif cnt == 3:
                satisfaction += 100
            elif cnt == 4:
                satisfaction += 1000

    return satisfaction

n = int(input())
like = {} # 좋아하는 학생번호
seats = [[0] * n for _ in range(n)] # 자리 배치도

for _ in range(n * n):
    lst = list(map(int, input().split()))
    student = lst[0]
    like[student] = lst[1:]

    emptySeat = find(like[student], seats, n)
    seats[emptySeat[0]][emptySeat[1]] = student # 자리 배치도에 학생 번호 넣기

print(calS(seats, like, n))
